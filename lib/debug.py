from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article


author_one=Author('Bakari isaac juma')
author_one.save()

found = Author.find_by_name('Bakari isaac juma')
print(found)

print("-----------------Testing Magazine model-----------------------------")
magazine_one=Magazine('Tech and Tune','Technology')
magazine_one.save()

find_magazine_by_name = Magazine.find_by_name('Tech and Tune')
print(find_magazine_by_name)

print("---------------------Testing article model-------------------------------------------")
article_one = Article('AI revolution in 2025',1,1)
article_one.save()
print(Article.find_by_title('AI revolution in 2025'))