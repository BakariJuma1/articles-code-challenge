from lib.db.connection import get_connection


class Author:

    def __init__(self,name,id=None):
        self.id = id
        self.name = name

    # inserting a new author in the db
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name) VALUES (?)",
            (self.name,)
        )
        conn.commit()
        self.id =cursor.lastrowid
        conn.close()

    # find author by id    # 
    @classmethod
    def find_by_id(cls,id):
         conn = get_connection()
         cursor=conn.cursor()
         cursor.execute("SELECT * FROM authors WHERE id = ?",(id,))
         row = cursor.fetchone()
         conn.close()
         return cls(row["name"],row["id"]) if row else None

    
    # finds author by name 
    @classmethod
    def find_by_name(cls,name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name = ?",(name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["name"],row["id"]) if row else None
    
    def __repr__(self):
        return (f"Author id ={self.id} name={self.name}")

