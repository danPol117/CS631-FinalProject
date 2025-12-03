import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("research_lab.db")

def run_sql_file(conn, filepath: str):
    path = Path(filepath)
    with path.open("r", encoding="utf-8") as f:
        script = f.read()
    conn.executescript(script)
    conn.commit()

def init_database():

    # Create the DB (overwrites when ran)
    conn = sqlite3.connect(DB_PATH)

    #Create tables
    run_sql_file(conn, "sql/schema.sql")

    #Insert sample data
    run_sql_file(conn, "sql/data.sql")

    conn.close()
    print("Success creating DB")

if __name__ == "__main__":
    init_database()
