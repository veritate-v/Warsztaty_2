from psycopg2 import connect


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

def create_db_connection(db_name):
    return connect(user=USER, password=PASSWORD, database=db_name, host=HOST)


create_db_connection('warsztaty_db')
