# articles-code-challenge

This project models a simple publishing system where **authors** write **articles** that appear in **magazines**. It’s built with plain Python and SQLite—no external frameworks—making it great for learning object-oriented programming and database relationships.

---

## 📌 What This Project Does

- Authors can write multiple articles.
- Magazines can publish many articles.
- Articles always belong to one author and one magazine.
- All data is saved in a SQLite database.
- Models have methods for creating, finding, updating, and deleting records.
- Relationships between models (like `author.articles()` or `magazine.contributors()`) are handled through SQL joins.

---

## 🏗️ Folder Structure

project/
├── lib/
│ ├── db/
│ │ └── connection.py # Handles SQLite database connection
│ └── models/
│ ├── author.py # Author model logic
│ ├── magazine.py # Magazine model logic
│ └── article.py # Article model logic
├── run_test.py # Optional test script
└── README.md # This file

yaml
Copy
Edit

---

## 🚀 How to Use

1. **Make sure you have Python 3 installed.**
2. Clone or download this project.
3. In your Python shell or script:

```python
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
Run create_table() on each class to create the database tables:

python
Copy
Edit
Author.create_table()
Magazine.create_table()
Article.create_table()
Start creating and linking objects:

python
Copy
Edit
author = Author("George Orwell")
magazine = Magazine("Politics Weekly", "Politics")
magazine.save()

article = author.add_article(magazine, "Big Brother Revisited")
🔍 Key Features
Author
Create or find authors by name or ID

Add new articles tied to magazines

Get all articles written by this author

List all magazines the author has contributed to

View the categories (topics) the author writes in

Get the top author based on article count

Magazine
Create magazines with name and category

Prevent duplicate magazine names

Get all articles published in a magazine

List contributors (authors) who’ve written for the magazine

Filter authors who’ve written more than two articles

Get all magazines with at least two unique contributors

Article
Create articles with validation (title must be 5+ characters)

Save, update, or delete articles

Look up articles by ID or title

🧪 Example Workflow
python
Copy
Edit
# Create the records
a = Author("Toni Morrison")
m = Magazine("Literary Voice", "Culture")
m.save()

# Add articles
a.add_article(m, "The Power of Language")
a.add_article(m, "Cultural Memory in Fiction")

# Explore relationships
print(a.articles())               # List of Article objects
print(m.contributors())           # List of Author objects
print(m.article_titles())         # List of article titles
print(a.topic_areas())            # ['Culture']
🗃️ Database Tables
sql
Copy
Edit
-- Authors
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- Magazines
CREATE TABLE magazines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT
);

-- Articles
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    magazine_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id),
    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
);
