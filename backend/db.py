import json
import os

from mssql_python import connect

CONNECTION_STRING = (
    f"Server={os.environ['DB_SERVER']};"
    f"Database={os.environ['DB_NAME']};"
    f"UID={os.environ['DB_ADMIN']};"
    f"PWD={os.environ['DB_ADMIN_PW']};"
    "Encrypt=yes;TrustServerCertificate=no;"
)


def get_conn():
    return connect(CONNECTION_STRING)


def upsert_user(google_sub, email, name):
    """Create the user on first login, refresh email/name after that. Returns users.id."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE dbo.users SET email = ?, name = ?, last_login_at = SYSUTCDATETIME() "
            "OUTPUT INSERTED.id WHERE google_sub = ?",
            (email, name, google_sub),
        )
        row = cur.fetchone()
        if row is None:
            cur.execute(
                "INSERT INTO dbo.users (google_sub, email, name) "
                "OUTPUT INSERTED.id VALUES (?, ?, ?)",
                (google_sub, email, name),
            )
            row = cur.fetchone()
        conn.commit()
        return row[0]


def save_madlib(user_id, words):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO dbo.madlibs (user_id, words) OUTPUT INSERTED.id VALUES (?, ?)",
            (user_id, json.dumps(words)),
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id


def get_madlib(user_id, madlib_id):
    """Fetch one saved madlib, only if it belongs to this user."""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT words FROM dbo.madlibs WHERE id = ? AND user_id = ?",
            (madlib_id, user_id),
        )
        row = cur.fetchone()
        return json.loads(row[0]) if row else None


def list_madlibs(user_id, limit=50):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT TOP (?) id, words, created_at FROM dbo.madlibs "
            "WHERE user_id = ? ORDER BY created_at DESC",
            (limit, user_id),
        )
        return [
            {"id": r[0], "words": json.loads(r[1]), "created_at": r[2]}
            for r in cur.fetchall()
        ]
