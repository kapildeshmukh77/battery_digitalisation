from datetime import datetime

from psycopg2 import pool


def _is_new_data(latest_inserted_static_data: dict[str, tuple], table_name: str, data: tuple) -> bool:
    """
    Check if the given data for a table is different from the last inserted data.
    Excludes the timestamp (assumed to be first element in data tuple).
    """
    # exclude timestamp
    last_data = latest_inserted_static_data.get(table_name)
    return data != last_data

def _get_data_without_timestamp(data: tuple) -> tuple:
    if not isinstance(data[0], datetime):
        raise ValueError('First Element of Data must be a datetime Timestamp')
    return data[1:]

class DatabaseConnector:
    def __init__(self, conn_params: dict):
        # Keeps track of which data was inserted last, so we dont store the same data multiple times
        self.latest_inserted_static_data: dict[str, tuple] = {}
        self.database_connection_pool = pool.SimpleConnectionPool(1, 20, **conn_params)

    def _update_latest_data(self, table_name: str, data: tuple):
        """Store the latest inserted data for a table (excluding timestamp)."""
        self.latest_inserted_static_data[table_name] = data

    def execute_static_insert(self,
                              sql_query: str,
                              sql_query_values: tuple,
                              static_table_name: str):
        data_without_timestamp = _get_data_without_timestamp(sql_query_values)
        if _is_new_data(self.latest_inserted_static_data, static_table_name, data_without_timestamp):
            insert_successful = self.execute_sql_query(sql_query, sql_query_values, static_table_name)

            if insert_successful:
                self._update_latest_data(static_table_name, data_without_timestamp)

    def execute_sql_query(self,
                          sql_query: str,
                          sql_query_values: tuple,
                          table_name: str) -> bool:
        """
        Runs an arbitrary sql query with parametrisation using a connection pool. Returns True if insert was successful
        """
        try:
            # Connect to the database using the connection pool
            conn = self.database_connection_pool.getconn()
            cursor = conn.cursor()
            cursor.execute(sql_query, sql_query_values)
            conn.commit()

        except Exception as e:
            print("Error inserting time-series data:", e)
            return False
        finally:
            # Release the connection back to the pool
            if conn:
                print(f'successfully inserted data into {table_name}')
                cursor.close()
                self.database_connection_pool.putconn(conn)
            return True


def build_insert_sql_query(data: dict, table_name: str) -> tuple[str, tuple]:
    # Extract field names and values
    fields = data.keys()
    values = tuple(data.values())

    # Create the SQL query
    placeholders = ', '.join(['%s'] * len(fields))  # Create placeholders for the values
    field_list = ', '.join(fields)  # Create a comma-separated list of fields

    insert_query = f'''
        INSERT INTO {table_name} ({field_list})
        VALUES ({placeholders})
    '''
    assert isinstance(values[0], datetime), ('First element must be datetime in order for `BFMDatabaseConnector` to'
                                             'work')
    return insert_query, values
