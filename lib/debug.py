from lib.models.author import Author
from lib.models.magazine import Magazine

author_one=Author('Bakari isaac juma')
author_one.save()

found = Author.find_by_name('Bakari isaac juma')
print(found)

magazine_one=Magazine('Tech and Tunez','Tech')
magazine_one.save()

find_magazine_by_name = Magazine.find_by_name('Tech and Tunez')
print(find_magazine_by_name)