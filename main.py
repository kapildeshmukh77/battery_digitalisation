import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Type

import pika

from digital_dryroom.config import get_psycopg2_conn_params, get_rabbit_mq_conn_params
from digital_dryroom.data_processing.channel import Channel
from digital_dryroom.data_processing.database_connection import DatabaseConnector, build_insert_sql_query
from digital_dryroom.data_processing.preprocess_data import reformat_data
from digital_dryroom.schema import (BFMStatic, BFMTimeSeries, EFMFillingStatic, EFMFillingTimeSeries, EFMGeneralStatic,
                                    EFMGeneralTimeSeries, EFMDegassingTimeSeries, EFMDegassingStatic, ZFSTimeSeries, ZFSStatic, Schema)


def make_default_data_handler(database_connector: DatabaseConnector,
                              static_schema: Type[Schema],
                              time_series_schema: Type[Schema]) -> callable:
    def handle_incoming_data(ch, method, _, body):
        """
        This is executed whenever there is new data in the rabbitMQ data queue.
        """
        data_dict = json.loads(body)
        static_data, time_series_data = reformat_data(data_dict, static_schema, time_series_schema)
        # Insert time series data
        sql_query, values = build_insert_sql_query(time_series_data, time_series_schema.get_table_name())
        database_connector.execute_sql_query(sql_query, values, time_series_schema.get_table_name())

        # Insert static data if changed
        sql_query, values = build_insert_sql_query(static_data, static_schema.get_table_name())
        database_connector.execute_static_insert(sql_query, values, static_schema.get_table_name())

        ch.basic_ack(delivery_tag=method.delivery_tag)
    return handle_incoming_data

def start_channel(queue_name: str, message_callback_function: callable) -> None:
    rabbit_mq_connection = get_rabbit_mq_connection()
    channel = rabbit_mq_connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_consume(queue=queue_name, on_message_callback=message_callback_function)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Stopping consumer...")
        channel.stop_consuming()
        rabbit_mq_connection.close()

def get_rabbit_mq_connection() -> pika.BlockingConnection:
    rabbit_mq_conn_params = get_rabbit_mq_conn_params()

    # Establish connection to RabbitMQ
    credentials = pika.PlainCredentials(rabbit_mq_conn_params['user'], rabbit_mq_conn_params['password'])
    connection_params = {'host': rabbit_mq_conn_params['host'],'credentials': credentials}
    if rabbit_mq_conn_params['vhost'] is not None:
        connection_params['virtual_host'] = rabbit_mq_conn_params['vhost']
    return pika.BlockingConnection(pika.ConnectionParameters(**connection_params))

global_database_connector = DatabaseConnector(get_psycopg2_conn_params())

channels = [
    Channel('bfm', BFMStatic, BFMTimeSeries),
    Channel('efm_filling', EFMFillingStatic, EFMFillingTimeSeries),
    Channel('efm_general', EFMGeneralStatic, EFMGeneralTimeSeries),
    Channel('efm_degassing', EFMDegassingStatic, EFMDegassingTimeSeries),
    Channel('zfs', ZFSStatic, ZFSTimeSeries)
]

with ThreadPoolExecutor(max_workers=len(channels)) as executor:
    channel_future_results = []
    for channel in channels:
        data_handler = make_default_data_handler(database_connector=global_database_connector,
                                                 static_schema=channel.static_schema,
                                                 time_series_schema=channel.time_series_schema)
        channel_future_result = executor.submit(start_channel, channel.rabbit_mq_que_name, data_handler)
        channel_future_results.append(channel_future_result)
    for future in as_completed(channel_future_results):
        try:
            future.result()
        except Exception as e:
            print(f"Channel crashed: {e}")