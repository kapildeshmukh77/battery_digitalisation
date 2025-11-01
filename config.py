PROD_DATABASE = True # Set to True if you work on the prod environment. Caution !!!
PROD_RABBITMQ = True

# TimescaleDB Connection Params
DB_NAME_DEV = "mydatabase"  # Change if your DB is hosted elsewhere
DB_USER_DEV = "user"
DB_PASS_DEV = "password"
DB_HOST_DEV = "localhost"
DB_PORT_DEV = '5432'

DB_NAME_PROD = "tsdb"  # Change if your DB is hosted elsewhere
DB_USER_PROD = "batt_admin"
DB_PASS_PROD = "gLW96UopGCbq78BfgGwX39Cs"
DB_HOST_PROD = "sxv20590.ise.fhg.de"
DB_PORT_PROD = '5432'

RABBITMQ_HOST_DEV = 'localhost'
RABBITMQ_USER_DEV = 'user'
RABBITMQ_PASS_DEV = 'password'

RABBIT_MQ_HOST_PROD = 'hub.ise.fraunhofer.de'
RABBITMQ_VHOST_PROD = 'dryroom'
RABBITMQ_USER_PROD = 'dryroom-admin'
RABBITMQ_PASS_PROD = 'GWrTXlHACGRMMZlmPhbIYoea'

def get_psycopg2_conn_params() -> dict:
    if PROD_DATABASE:
        return {
            'dbname': DB_NAME_PROD,
            'user': DB_USER_PROD,
            'password': DB_PASS_PROD,
            'host': DB_HOST_PROD,
            'port': DB_PORT_PROD
        }
    return  {
        'dbname': DB_NAME_DEV,
        'user': DB_USER_DEV,
        'password': DB_PASS_DEV,
        'host': DB_HOST_DEV,
        'port': DB_PORT_DEV
    }


def get_rabbit_mq_conn_params() -> dict:
    if PROD_RABBITMQ:
        return {
            'host': RABBIT_MQ_HOST_PROD,
            'vhost': RABBITMQ_VHOST_PROD,
            'user': RABBITMQ_USER_PROD,
            'password': RABBITMQ_PASS_PROD,
        }
    return {
            'host': RABBITMQ_HOST_DEV,
            'vhost': None,
            'user': RABBITMQ_USER_DEV,
            'password': RABBITMQ_PASS_DEV,
        }
