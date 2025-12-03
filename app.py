import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("research_lab.db")

def get_connection():
    #Create connection to DB file
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  
    """Description of what the line right above this does
    
    Basically, it allows us to access the whatever the query fetches by col name 

    Without this line, it would return tuples like (0,Daniel,...,...,...), and we would have to access the cols 
    using things like row[0], row[1], which is annoying since you have to memorize positions

    With this line, queries return dicts like this {'member_id': 0, 'name': 'Daniel'}, and allows us 
    to access data like so row["name"] and so on, which is better
    """
    return conn

def list_members():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM Member")
    rows = cur.fetchall()

    conn.close()

    print("Members:")
    for row in rows:
        print(f"{row['MID']}: {row['name']}")


if __name__ == "__main__":
    list_members()
