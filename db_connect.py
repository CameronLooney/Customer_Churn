import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import io
def connect_postgres():
    conn = psycopg2.connect(
        host="localhost",
        database="covid",
        user="cameron",
        password="root")
    return conn


def import_data(path):
    df = pd.read_csv(path)
    return df





def csv_to_postgres(pg_user, pg_password, pg_host, pg_database,pg_port ,csv_path,pg_tablename):
    try:
        engine = create_engine('postgresql+psycopg2://{}:{}@{}:{}/{}'.format(pg_user, pg_password, pg_host,pg_port, pg_database))
        print("Connected to Postgres")
        df = import_data(csv_path)
        print("Data imported")
        df.head(0).to_sql(pg_tablename, engine, if_exists='replace',index=False) #drops old table and creates new empty table

        conn = engine.raw_connection()
        cur = conn.cursor()
        print("cursor created")
        output = io.StringIO()
        df.to_csv(output, sep='\t', header=False, index=False)
        output.seek(0)
        print("seeking output....")
        contents = output.getvalue()
        cur.copy_from(output, pg_tablename, null="") # null values become ''
        conn.commit()
        cur.close()
    except:
        print("Error in writing to postgres")


#csv_to_postgres("cameron", "root", "localhost", "ibm_churn", 5432, "/Users/cameronlooney/Documents/IBM-Telco.csv","churn")
csv_to_postgres("cameron", "root", "localhost", "odq", 5432, "/Users/cameronlooney/Documents/autopivot.csv","autopivot")
csv_to_postgres("cameron", "root", "localhost", "odq", 5432, "/Users/cameronlooney/Documents/backlog.csv","backlog_pivot")