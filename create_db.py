import sys
from typing import Type

import psycopg2

from digital_dryroom.config import get_psycopg2_conn_params, PROD_DATABASE
from digital_dryroom.helper import python_type_to_sql
from digital_dryroom.schema import Schema, all_schemas
from digital_dryroom.schema.efm import (EFMFillingStatic, EFMGeneralStatic, EFMGeneralTimeSeries, EFMFillingTimeSeries,
                                        EFMDegassingStatic, EFMDegassingTimeSeries)
from digital_dryroom.schema.zfs import (ZFSStatic, ZFSTimeSeries)


def generate_create_table_sql(db_schema: Type[Schema]) -> str:
    """
    Creates Database create table query using the schema defined by a dataclass.
    """
    sql_command = [f"CREATE TABLE IF NOT EXISTS {db_schema.get_table_name()} ("]
    for field in db_schema.get_fields():
        sql_type = python_type_to_sql(field.type)
        pk = " PRIMARY KEY" if field.name == 'timestamp' else ""
        sql_command.append(f"    {field.name} {sql_type}{pk},")

    sql_command[-1] = sql_command[-1].rstrip(",")  # remove trailing comma
    sql_command.append(");")
    if db_schema.is_timeseries():
        sql_command.append(f"SELECT create_hypertable('{db_schema.get_table_name()}', 'timestamp');")

    return "\n".join(sql_command)

def init_db_with_schemas(schemas: list[Type[Schema]]):
    for schema in schemas:
        create_db_table(schema)


def generate_alter_table_sql(db_schema: Type[Schema]) -> str:
    sql_command = []

    for field in db_schema.get_fields():
        column_exists = check_column_exists(db_schema.get_table_name(), field.name)
        if not column_exists:
            sql_type = python_type_to_sql(field.type)
            sql_command.append(f"ALTER TABLE {db_schema.get_table_name()} ADD COLUMN {field.name} {sql_type};")

    return "\n".join(sql_command)

def check_column_exists(table_name: str, column_name: str) -> bool:
    query = f"""
    SELECT EXISTS (
        SELECT 1 
        FROM information_schema.columns 
        WHERE table_name = '{table_name}' 
        AND column_name = '{column_name}'
    );
    """
    try:
        conn = psycopg2.connect(**get_psycopg2_conn_params())
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        print("Error checking column existence:", e)
        return False
    finally:
        cursor.close()
        conn.close()


def alter_db_table(schema: Type[Schema]):
    try:
        conn = psycopg2.connect(**get_psycopg2_conn_params())
        cursor = conn.cursor()

        # Generate the ALTER TABLE query
        alter_query = generate_alter_table_sql(schema)
        if alter_query:
            print("Executing the following ALTER TABLE queries:")
            print(alter_query)
            cursor.execute(alter_query)
            conn.commit()
        else:
            print("No changes detected. Skipping ALTER TABLE.")

    except Exception as e:
        print("Error altering table:", e)
    finally:
        cursor.close()
        conn.close()

def create_db_table(schema: Type[Schema]):
    if PROD_DATABASE:
        print(
            "You are working on the prod database!!!! Exiting program. "
            "If you are sure what you are doing, remove this safeguard."
        )
        sys.exit(1)
    try:
        # Connect to the database
        conn = psycopg2.connect(**get_psycopg2_conn_params())
        cursor = conn.cursor()

        creation_query = generate_create_table_sql(schema)
        print(creation_query)
        cursor.execute(creation_query)
        conn.commit()

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_db_with_schemas([EFMFillingStatic, EFMGeneralStatic, EFMGeneralTimeSeries, EFMFillingTimeSeries,
                                        EFMDegassingStatic, EFMDegassingTimeSeries, ZFSTimeSeries, ZFSStatic])

    #alter_db_table(EFMFillingTimeSeries)
    alter_db_table(ZFSTimeSeries)
