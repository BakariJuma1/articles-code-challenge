from lib.db.connection import get_connection



class Author:

    def __init__(self,name,id=None):
        if not name:
            raise ValueError("Author name is required")
        
        self.id = id
        self._name = name
        self.save()

    @property
    def name(self):
        return self._name
    

    # inserting a new author in the db
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO authors (name) VALUES (?)",
            (self._name,)
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
     
    #  return all articles written by this author
    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row["title"], row["author_id"], row["magazine_id"], row["id"]) for row in rows]
    
    #Return all unique magazines this author has written for
    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(row["name"], row["category"], row["id"]) for row in rows]  
    
    
    #Create and save a new article for this author and given magazine
    def add_article(self, magazine, title):
        from lib.models.article import Article
        article = Article(title, self.id, magazine.id)
        article.save()
        return article

    #Return a list of unique magazine categories this author has written in
    def topic_areas(self):
       
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [row["category"] for row in rows]
    
    @classmethod
    def top_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
           SELECT a.*, COUNT(ar.id) AS article_count
                         FROM authors a
           JOIN articles ar ON a.id = ar.author_id
           GROUP BY a.id
           ORDER BY article_count DESC
           LIMIT 1
         """)
        row = cursor.fetchone()
        conn.close()
        if row:
          return cls(row["name"], row["id"])
        return None


    
    def __repr__(self):
        return (f"Author id ={self.id} name={self.name}")

