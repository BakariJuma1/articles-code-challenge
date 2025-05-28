from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author_id, magazine_id, id=None):
        if not title or len(title) < 5:
            raise ValueError("Title must be at least 5 characters")
        
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

        if self.id is None:
            self.save()

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
            (self.title, self.author_id, self.magazine_id)
        )
        conn.commit()
        self.id = cursor.lastrowid
        conn.close()

    def update(self):
        if self.id is None:
            raise ValueError("Cannot update unsaved article")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
            (self.title, self.author_id, self.magazine_id, self.id)
        )
        conn.commit()
        conn.close()

    def delete(self):
        if self.id is None:
            raise ValueError("Cannot delete unsaved article")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
        self.id = None

    @classmethod
    def create_table(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author_id INTEGER,
                magazine_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(id)
            )
        """)
        conn.commit()
        conn.close()

    @classmethod
    def drop_table(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS articles")
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()
        conn.close()
        return [cls(row["title"], row["author_id"], row["magazine_id"], row["id"]) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["title"], row["author_id"], row["magazine_id"], row["id"]) if row else None

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title = ?", (title,))
        row = cursor.fetchone()
        conn.close()
        return cls(row["title"], row["author_id"], row["magazine_id"], row["id"]) if row else None

    def __repr__(self):
        return f"Article(id={self.id}, title={self.title})"
