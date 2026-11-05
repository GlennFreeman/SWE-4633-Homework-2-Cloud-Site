import sqlite3
from sqlite3 import Connection, Cursor

con: Connection = sqlite3.connect("tutorial.db")
cur: Cursor = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        issuer TEXT NOT NULL,
        sub TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        name TEXT,
        picture TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        last_login_at TEXT DEFAULT CURRENT_TIMESTAMP,

        -- Prevents duplicate accounts for the same provider ID
        UNIQUE(issuer, sub)
    )
""")

con.commit()
con.close()
