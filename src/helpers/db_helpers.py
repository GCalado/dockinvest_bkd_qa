import os
import psycopg2

def set_database_credentials(db_name):
    database_credentials = {
      "host": os.environ[f"{db_name}_host"],
      "port": os.environ[f"{db_name}_port"],
      "dbname": os.environ[f"{db_name}_dbname"],
      "username": os.environ[f"{db_name}_username"],
      "password": os.environ[f"{db_name}_password"]
    }
    return database_credentials

def run_postgres_select(bd_credentials, query):
    conn = psycopg2.connect(
        host=bd_credentials['host'],
        port=bd_credentials['port'],
        dbname=bd_credentials['dbname'],
        user=bd_credentials['username'],
        password=bd_credentials['password']
    )
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            results = cur.fetchall()
        return results
    finally:
        conn.close()