from lib.db.connection import get_connection

class Article:
    def __init__(self,title,author_id,magazine_id,id=None):
        self.id = id 
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    # insert article into db    #
    def save(self):
        conn = get_connection() 
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title,author_id,magazine_id) VALUES (?,?,?)",
            (self.title,self.author_id,self.magazine_id)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @classmethod
    def find_by_id(cls,id):
        conn=get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?",(id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["title"],row["author_id"],row["magazine_id"],row["id"]) if row else None
    
    
    @classmethod
    def find_by_title(cls,title):
        conn=get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?",(title,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["title"],row["author_id"],row["magazine_id"],row["id"]) if row else None
    
    def __repr__(self):
        return(f"article id={self.id} title={self.title}")