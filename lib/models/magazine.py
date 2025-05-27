from lib.db.connection import get_connection


class Magazine:
    def __init__(self, name, category, id=None):
        if not name:
            raise ValueError("Magazine name is required")
        self.id = id
        self._name = name
        self.category = category

    @property
    def name(self):
        return self._name    

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Uniqueness check before saving
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (self._name,))
        if cursor.fetchone():
            conn.close()
            raise ValueError("Magazine name must be unique")

        cursor.execute(
            "INSERT INTO magazines (name, category) VALUES (?, ?)",
            (self._name, self.category)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    @classmethod 
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["name"], row["category"], row["id"]) if row else None
    
    @classmethod 
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["name"], row["category"], row["id"]) if row else None
    
    @classmethod 
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(row["name"], row["category"], row["id"]) for row in rows]

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(row["title"], row["author_id"], row["magazine_id"], row["id"]) for row in rows]   
    
    def contributors(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row["name"], row["id"]) for row in rows]
        
    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        from lib.models.author  import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.*, COUNT(ar.id) as article_count
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Author(row["name"], row["id"]) for row in rows]
    
    def __repr__(self):
        return f"<Magazine id={self.id}, name='{self.name}', category='{self.category}'>"
