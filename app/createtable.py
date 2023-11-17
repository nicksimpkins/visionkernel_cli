def create_custom_table(connection, table_name):
    try:
        with connection.cursor() as cursor:
            # Define your custom table creation SQL statement
            # Adjust the SQL statement based on your table schema
            table_creation_sql = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id VARCHAR(255) PRIMARY KEY,
                    column1 VARCHAR(255),
                    column2 VARCHAR(255)
                    -- Add more columns as needed
                );
            """

            # Execute the SQL statement
            cursor.execute(table_creation_sql)

        # Commit the transaction
        connection.commit()

        print(f"Table '{table_name}' created successfully!")

    except Exception as e:
        print(f"Error creating table: {e}")

def list_tables(connection):
    try:
        with connection.cursor() as cursor:
            # Define SQL query to list all tables
            list_tables_sql = """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """

            # Execute the SQL query
            cursor.execute(list_tables_sql)

            # Fetch all table names
            existing_tables = [row[0] for row in cursor.fetchall()]

        return existing_tables

    except Exception as e:
        print(f"Error listing tables: {e}")
        return []
