import os

import mssql_python as mssql
from dotenv import load_dotenv
from mssql_python import Connection, Cursor, DatabaseError

load_dotenv()

connection_string = (
    f"Server={os.environ['DB_SERVER']};"
    f"Database={os.environ['DB_NAME']};"
    f"UID={os.environ['DB_ADMIN']};"
    f"PWD={os.environ['DB_ADMIN_PW']};"
    "Encrypt=yes;TrustServerCertificate=no;"
)

try:
    print("Connecting to Azure SQL Database...")

    con: Connection = mssql.connect(connection_string)
    cur: Cursor = con.cursor()

    cur.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Users' AND xtype='U')
        CREATE TABLE Users (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            email VARCHAR(50) UNIQUE
        )
    """)
    print("Table verified/created.")

    # 2. Insert dummy data
    cur.execute(
        "INSERT INTO Users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com")
    )
    con.commit()  # Commit transaction to save changes
    print("Data inserted successfully.")

    # 3. Query the data
    cur.execute("SELECT id, name, email FROM Users")
    rows = cur.fetchall()

    print("\n--- Database Records ---")
    for row in rows:
        print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")

    # Clean up connections
    cur.close()
    con.close()
    print("\nConnection closed safely.")

except DatabaseError as e:
    print(e)

finally:
    # Clean up connections
    cur.close()
    con.close()
    print("\nConnection closed safely.")
