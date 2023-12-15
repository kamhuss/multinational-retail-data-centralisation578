#Step 2: Create a method read_db_creds


import yaml
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import inspect

class DatabaseConnector:
    def __init__(self):
        self.read_db_creds = DatabaseConnector.read_db_creds()
        self.db_engine = DatabaseConnector.init_db_engine()
    
    def read_db_creds():
        with open('db_creds.yaml', 'r') as file:
            db_creds = yaml.safe_load(file)
        return db_creds

#Step 3: Create a method init_db_engine

    def init_db_engine(self):
        self.db_creds = DatabaseConnector.read_db_creds
        db_creds = DatabaseConnector.read_db_creds()
        db_url = db_url = f"postgresql://{db_creds['RDS_USER']}:{db_creds['RDS_PASSWORD']}@{db_creds['RDS_HOST']}:{db_creds['RDS_PORT']}/{db_creds['RDS_DATABASE']}"
        engine = create_engine(db_url)
        return engine

#Step 4: Create a method list_db_tables

    def list_db_tables():
        engine = DatabaseConnector.init_db_engine()
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        return tables
     
#Step 7: Create a method upload_to_db in the DatabaseConnector class

    def upload_to_db(df, table_name):
        engine = DatabaseConnector.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)

def read_rds_table(table_name):
        db_connector = DatabaseConnector()
        engine = db_connector.init_db_engine()

        # Use pandas to read the table into a DataFrame
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql_query(query, engine)
        return df



