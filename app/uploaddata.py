import pandas as pd
import psycopg2
import numpy as np
from psycopg2.extensions import register_adapter, AsIs

# Register adapters for numpy types
register_adapter(np.int64, AsIs)
register_adapter(np.float64, AsIs)

def upload_excel_data(connection, table_name, excel_file_path):
    try:
        # Read Excel file into a Pandas DataFrame
        df = pd.read_excel(excel_file_path)

        # Convert NaN values to None
        df = df.where(pd.notna(df), None)

        # Create a list of tuples from the DataFrame
        records = [tuple(row) for row in df.to_records(index=False)]

        # Prepare the SQL query for insertion
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"

        with connection.cursor() as cursor:
            # Execute the SQL query for insertion
            cursor.executemany(insert_query, records)

        # Commit the transaction
        connection.commit()

        print(f"Data uploaded successfully to table '{table_name}'!")

    except Exception as e:
        print(f"Error uploading data: {e}")
