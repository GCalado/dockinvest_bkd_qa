import psycopg2

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