#Step 5: Create a method read_rds_table in your DataExtractor class

import pandas as pd
from database_utils import DatabaseConnector
import tabula
import requests
import boto3
import json

class DataExtractor:
    def read_rds_table(table_name):
        db_connector = DatabaseConnector()
        engine = db_connector.init_db_engine()

        # Use pandas to read the table into a DataFrame
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql_query(query, engine)
        return df

# ms2 task 4 step 2

    def retrieve_pdf_data():
        pdf_path = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
        dfs = tabula.read_pdf(pdf_path, stream=True)
        return dfs

# ms2 task 5 step 1-3


    header_details = {
    'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'
}

    endpoints = {
    'retrieve_store': 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}',
    'number_of_stores': 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
}


    def __init__(self, api_key):
        self.header = {'x-api-key': api_key}

    def list_number_of_stores(self, number_of_stores_endpoint):
        response = requests.get(number_of_stores_endpoint, headers=self.header)
        return response.json().get('number_of_stores')

    def retrieve_stores_data(self, retrieve_store_endpoint):
        response = requests.get(retrieve_store_endpoint, headers=self.header)
        return response.json()

# ms2 task 6 step 1

    def __init__(self):
        self.s3_client = boto3.client('s3')

    def extract_from_s3(self, s3_address):
        bucket_name, key = self.parse_s3_address(s3_address)
        response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
        df = pd.read_csv(response['Body'])
        return df

    def parse_s3_address(s3_address):
        s3_parts = s3_address.replace('s3://', '').split('/')
        bucket_name = s3_parts[0]
        key = '/'.join(s3_parts[1:])
        return bucket_name, key
    
# ms2 task 8

    def __init__(self):
        self.s3_client = boto3.client('s3')

    def extract_from_s3_json(self, s3_address):
        bucket_name, key = self.parse_s3_address(s3_address)
        response = self.s3_client.get_object(Bucket=bucket_name, Key=key)
        json_data = json.load(response['Body'])
        df = pd.json_normalize(json_data)
        return df

   
    def parse_s3_address(s3_address):
    
        s3_parts = s3_address.replace('https://', '').split('/')
        bucket_name = s3_parts[0]
        key = '/'.join(s3_parts[1:])
        return bucket_name, key