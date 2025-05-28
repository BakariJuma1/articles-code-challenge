Articles Code Challenge
This project is a simple aricle  management system built using Python and SQLite.

 #Features
🔁 Full CRUD Support for Author and Magazine models — Create, Read, Update, and Delete with ease.

🧾 Relational Article Model — Articles are always linked to both an author and a magazine.

🔗 Smart Relationship Methods — Use SQL joins under the hood to fetch related data like an author's magazines or a magazine’s contributors.

🔒 Safe Transactions — Articles can be batch-created with authors in one atomic, rollback-safe operation.


Setup
Clone the repo
git clone git@github.com:mbxisbankai/articles-code-challenge.git
Create and activate a virtual environment
pipenv install && pipenv shell
Install dependencies using pip install -r requirements.txt or via Pipenv
pipenv install sqlite3
Initialize the database by running
python3 scripts/setup_db.py
Run python3 debug.py to populate the database with sample data 
