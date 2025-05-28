# 📰 Articles Code Challenge

Welcome to the **Articles Code Challenge**! This is a simple yet powerful content management system built using **Python** and **SQLite**. It allows you to create, associate, and manage **Authors**, **Magazines**, and their published **Articles** — all while practicing raw SQL and object relationships.

---

## 👨🏾‍💻 Developer

**Bakari Isaac Juma**  
Fullstack Software Engineering Student @ Moringa School  
Passionate about clean code, real-world problem solving, and building cool things with Python 🐍 and JavaScript ⚡

---

## 🌟 Features

- ✅ Full CRUD operations for **Author** and **Magazine** models
- 📝 Articles can be created and linked to both Authors and Magazines
- 🔄 SQL-powered relationship methods for retrieving related data
- 💾 Transaction-safe article creation using raw SQL and Python classes
- 🎯 Lightweight and easy to run locally

---

## 🛠 Setup Instructions

Follow these steps to get the project up and running on your machine:

### 1. Clone the repo

```bash
git clone git@github.com:Bakari-juma/articles-code-challenge.git
cd articles-code-challenge
2. Set up your virtual environment
If you're using Pipenv:

bash
Copy
Edit
pipenv install && pipenv shell
Or if you’re using venv and pip:

bash
Copy
Edit
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
3. Install SQLite3 (if not already installed)
bash
Copy
Edit
pipenv install sqlite3
4. Initialize the database
bash
Copy
Edit
python3 scripts/setup_db.py
5. Seed the database with sample data
bash
Copy
Edit
python3 db/seed.py
You're now ready to play around with the system, run queries, and explore relationships between authors, magazines, and articles.

