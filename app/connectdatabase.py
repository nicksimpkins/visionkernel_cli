import boto3
import psycopg2
import pyodbc
from google.cloud import storage

def connect_to_aws_rds(database_name, username, password, database_endpoint, port):
    try:

        conn = psycopg2.connect(
            database=database_name,
            user=username,
            password=password,
            host=database_endpoint,
            port=int(port),
        )

        print("Connected to the AWS RDS database successfully!")
        return conn

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def connect_to_azure_sql(server_name, database_name, username, password):
    try:
        connection_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server_name}.database.windows.net;Database={database_name};UID={username};PWD={password};"
        conn = pyodbc.connect(connection_str)

        print("Connected to Azure SQL Database successfully!")
        return conn

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def connect_to_google_cloud_sql(instance_connection_name, database_name, username, password):
    try:
        conn = psycopg2.connect(
            user=username,
            password=password,
            host=f"/cloudsql/{instance_connection_name}",
            database=database_name
        )

        print("Connected to Google Cloud SQL Database successfully!")
        return conn

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def connect_to_google_cloud_storage(bucket_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        print(f"Connected to Google Cloud Storage bucket '{bucket_name}' successfully!")
        return bucket

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def create_table_postgresql(connection, table_name, column_definitions):
    try:
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Table '{table_name}' created successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def create_table_azure_sql(connection, table_name, column_definitions):
    try:
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Table '{table_name}' created successfully in Azure SQL Database!")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def create_table_gcloud_sql(connection, table_name, column_definitions):
    try:
        cursor = connection.cursor()
        create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Table '{table_name}' created successfully in Google Cloud SQL Database!")

    except Exception as e:
        print(f"An error occurred: {e}")
        return None