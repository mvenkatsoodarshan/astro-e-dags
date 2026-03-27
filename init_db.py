import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    gm TEXT,
    child TEXT,
    source TEXT,
    active INTEGER,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert sample
cursor.execute("""
INSERT INTO jobs (gm, child, source, active)
VALUES ('GM1', 'C1', 'S1', 1)
""")

conn.commit()
conn.close()