from lib.db.connection import get_connection

class Magazine:
    def __init__(self,name,category,id=None):
        self.id = id
        self.name = name
        self.category = category

    # inserts new magazine into the db    # 
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO magazines (name,category) vALUES (?,?)",
            (self.name,self.category)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    # find magazine by id    #
    @classmethod 
    def find_by_id(cls,id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM magazines WHERE id = ?",((id,))
        )
        row = cursor.fetchone()
        conn.close()
        return cls(row["name"],row["category"],row["id"]) if row else None
    
    # find magazine by name    #
    @classmethod 
    def find_by_name(cls,name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM magazines WHERE name = ?",((name,))
        )
        row = cursor.fetchone()
        conn.close()
        return cls(row["name"],row["category"],row["id"]) if row else None
    
    # find magazine by category   #
    @classmethod 
    def find_by_id(cls,category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM magazines WHERE category = ?",((category,))
        )
        row = cursor.fetchall()
        conn.close()
        return cls(row["name"],row["category"],row["id"]) if row else None
    
    def __repr__(self):
        return (f"magazine id = {self.id} name={self.name} category={self.category}")

