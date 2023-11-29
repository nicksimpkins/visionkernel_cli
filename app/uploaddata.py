import pandas as pd
import psycopg2

def get_postgresql_data_type(pandas_dtype):
    """Maps pandas data types to PostgreSQL data types."""
    if pandas_dtype.name.startswith('int'):
        return 'INTEGER'
    elif pandas_dtype.name.startswith('float'):
        return 'REAL'  # or 'DOUBLE PRECISION' for higher precision
    elif pandas_dtype.name.startswith('datetime'):
        return 'TIMESTAMP'
    elif pandas_dtype.name.startswith('bool'):
        return 'BOOLEAN'
    else:
        return 'VARCHAR'  # Default to VARCHAR for other types

def auto_create_table_from_excel(connection, table_name, excel_file_path, sheet_name=None):
    try:
        # Read Excel file into a Pandas DataFrame
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # Start creating the SQL statement
        create_table_sql = f"CREATE TABLE {table_name} ("

        # Generate column definitions
        column_definitions = []
        for col in df.columns:
            # Format column name for SQL (replace spaces, etc.)
            formatted_col = col.replace(" ", "_").lower()
            col_data_type = get_postgresql_data_type(df[col].dtype)
            column_definitions.append(f"{formatted_col} {col_data_type}")

        # Combine column definitions and complete SQL statement
        create_table_sql += ', '.join(column_definitions) + ");"

        # Execute the SQL statement to create a new table
        with connection.cursor() as cursor:
            cursor.execute(create_table_sql)
            connection.commit()

        print(f"Table '{table_name}' created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")


def upload_excel_data(connection, table_name, excel_file_path, sheet_name=None):
    try:
        # Read Excel file into a Pandas DataFrame
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # Format column names (convert to lowercase) and create SQL statement
        formatted_columns = [f'"{col.lower()}"' for col in df.columns]
        columns = ', '.join(formatted_columns)
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"

        # Convert NaN values to None
        df = df.where(pd.notna(df), None)

        # Create a list of tuples from the DataFrame
        records = [tuple(row) for row in df.to_records(index=False)]

        with connection.cursor() as cursor:
            # Execute the SQL query for insertion
            cursor.executemany(insert_query, records)

        # Commit the transaction
        connection.commit()

        print(f"Data uploaded successfully to table '{table_name}'!")

    except Exception as e:
        print(f"Error uploading data: {e}")