from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.models.article import Article

def print_menu():
    print("\n=== Articles App ===")
    print("1. Create Author")
    print("2. Create Magazine")
    print("3. Create Article")
    print("4. List Articles by Author")
    print("5. List Magazines by Author")
    print("6. Show Magazine Article Titles")
    print("7. Show Magazine Contributors")
    print("8. Show Magazine Contributing Authors (>2 articles)")
    print("9. Show Author's Topic Areas")
    print("0. Exit")

def main():
    authors = []
    magazines = []

    while True:
        print_menu()  
        choice = input("choose an option:")

        try:
            if choice== '1':
                name = input("Enter the authors name:")
                author=Author(name)
                authors.append(author)
                print("Author created succesfully")

            elif choice =="2":
                name = input('Enter magazine name:')  
                category = input('Enter category')
                magazine = Magazine(name,category)
                magazines.append(magazine)
                print("Magazine created") 

            elif choice == "3":
                if not authors or not magazines:
                    print("you need atleast one author and one magazine.") 
                    continue
                print("Authors")
                for i,a in enumerate(authors):
                    print(f"{i + 1}.{a.name}")
                author_index = int(input("Choose aurthor:")) -1 

                print("Magazines")
                for i, m in enumerate(magazines):
                    print(f"{i + 1}. {m.name}")
                magazine_index = int(input("Choose magazine #: ")) - 1

                title = input("Enter article title: ")
                Article(title, authors[author_index], magazines[magazine_index])
                print("Article created!")

        except Exception as e:
            print(f"Error:{e}")        

if __name__ == "__main__":
    main()
