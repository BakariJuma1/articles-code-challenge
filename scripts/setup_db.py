from lib.db.connection import get_connection

def setup_db():
    conn= get_connection()
    with open('lib/db/schema.sql','r') as f:
        conn.executescript(f.read())
    print('Database setup success')
    conn.close()

if __name__ == "__main__":
    setup_db()    
