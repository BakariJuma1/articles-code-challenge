from lib.models.author import Author

author_one=Author('Bakari isaac juma')
author_one.save()

found = Author.find_by_name('Bakari isaac juma')
print(found)