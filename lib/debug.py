from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article


conn = get_connection()
cursor = conn.cursor()

# Delete existing magazine named 'Tech and Tune' before tests
cursor.execute("DELETE FROM magazines WHERE name = ?", ('Tech and Tune',))
conn.commit()
conn.close()

author_one = Author('Bakari isaac juma')

found = Author.find_by_name('Bakari isaac juma')
print(found)

print("-----------------Testing Magazine model-----------------------------")
magazine_one = Magazine('Tech and Tune', 'Technology')
magazine_one.save()

find_magazine_by_name = Magazine.find_by_name('Tech and Tune')
print(find_magazine_by_name)

print("---------------------Testing article model-------------------------------------------")
article_one = Article('AI revolution in 2025', 1, 1)
article_one.save()
print(Article.find_by_title('AI revolution in 2025'))

articles_to_add = [
    {'title': 'Understanding SQL Transactions', 'magazine_id': 1},
    {'title': 'Advanced Python SQL', 'magazine_id': 2},
]

success = Author.add_author_with_articles("Steve biko", articles_to_add)
if success:
    print("Author and articles added successfully!")
else:
    print("Failed to add author and articles.")
