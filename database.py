import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Create table for storing emails
cursor.execute("""
CREATE TABLE IF NOT EXISTS emails (
    id TEXT PRIMARY KEY,
    sender TEXT,
    recipient TEXT,
    subject TEXT,
    received_at TEXT,
    snippet TEXT,
    is_read BOOLEAN DEFAULT FALSE
)
""")

conn.commit()
conn.close()

print("✅ Database and table created successfully.")
