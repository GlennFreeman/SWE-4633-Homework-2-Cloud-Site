import sqlite3
from sqlite3 import Connection, Cursor

con: Connection = sqlite3.connect("dev.db")
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

        UNIQUE(issuer, sub)
    )
""")
con.commit()

# Mock payload received from an OIDC ID Token
oidc_profile = {
    "issuer": "https://google.com",
    "sub": "google-user-123456",
    "email": "user@example.com",
    "name": "Alex Doe",
    "picture": "https://example.com",
}

# The UPSERT SQL Statement
upsert_query = """
    INSERT INTO users (issuer, sub, email, name, picture)
    VALUES (:issuer, :sub, :email, :name, :picture)
    ON CONFLICT(issuer, sub) DO UPDATE SET
        name = excluded.name,
        picture = excluded.picture,
        last_login_at = CURRENT_TIMESTAMP
"""

cur.execute(upsert_query, oidc_profile)
con.commit()

con.close()
