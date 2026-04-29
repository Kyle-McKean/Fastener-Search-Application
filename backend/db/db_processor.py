# File to convert the .xlsx file to a .db file
import pandas as pd
import sqlite3

def convert_xlsx_to_db(xlsx_file, db_file):
    # Read the Excel file
    df = pd.read_excel(xlsx_file)

    # print(df.head())  # Print the first few rows of the DataFrame to verify it was read correctly

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_file)

    # Create table from schema.sql to ensure consistency with the expected database structure
    with open('backend\\db\\schema.sql', 'r') as f:
        conn.executescript(f.read())


    # Write the DataFrame to the SQLite database
    df.to_sql('fasteners', conn, if_exists='replace', index=False)

    
    # Verify that the data was written to the database using a cursor
    # cursor = conn.cursor()

    # # cursor.execute(""" SELECT *  FROM data """)

    # result = cursor.fetchone()
    # print(result)


    # Close the connection
    conn.close()


xlsx_file = "backend\db\FastenerDataset.xlsx"  # Path to your .xlsx file
db_file = "backend\\db\\fastener_data.db"  # Path to your .db file

convert_xlsx_to_db(xlsx_file, db_file)

