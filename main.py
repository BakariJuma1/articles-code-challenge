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

def select_author(authors):
    if not authors:
        print("No authors available.")
        return None
    print("Authors:")
    for i, a in enumerate(authors):
        print(f"{i + 1}. {a.name}")
    try:
        choice = int(input("Choose author: ")) - 1
        if choice not in range(len(authors)):
            print("Invalid author choice.")
            return None
        return authors[choice]
    except ValueError:
        print("Please enter a valid number.")
        return None

def select_magazine(magazines):
    if not magazines:
        print("No magazines available.")
        return None
    print("Magazines:")
    for i, m in enumerate(magazines):
        print(f"{i + 1}. {m.name}")
    try:
        choice = int(input("Choose magazine: ")) - 1
        if choice not in range(len(magazines)):
            print("Invalid magazine choice.")
            return None
        return magazines[choice]
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    authors = []
    magazines = []

    # Load existing authors and magazines from DB if needed
    # For simplicity, this example uses only runtime created objects

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == '1':
                name = input("Enter the author's name: ").strip()
                author = Author(name)
                authors.append(author)
                print(f"Author '{author.name}' created successfully.")

            elif choice == '2':
                name = input("Enter magazine name: ").strip()
                category = input("Enter category: ").strip()
                magazine = Magazine(name, category)
                magazines.append(magazine)
                print(f"Magazine '{magazine.name}' created successfully.")

            elif choice == '3':
                if not authors or not magazines:
                    print("You need at least one author and one magazine before creating articles.")
                    continue
                author = select_author(authors)
                if not author:
                    continue
                magazine = select_magazine(magazines)
                if not magazine:
                    continue
                title = input("Enter article title: ").strip()
                article = Article(title, author.id, magazine.id)
                article.save()
                print(f"Article '{title}' created successfully.")

            elif choice == '4':  # List Articles by Author
                author = select_author(authors)
                if not author:
                    continue
                articles = author.articles()
                if not articles:
                    print(f"No articles found for author '{author.name}'.")
                else:
                    print(f"Articles by {author.name}:")
                    for art in articles:
                        print(f"- {art.title}")

            elif choice == '5':  # List Magazines by Author
                author = select_author(authors)
                if not author:
                    continue
                magazines_list = author.magazines()
                if not magazines_list:
                    print(f"No magazines found for author '{author.name}'.")
                else:
                    print(f"Magazines for {author.name}:")
                    for mag in magazines_list:
                        print(f"- {mag.name} ({mag.category})")

            elif choice == '6':  # Show Magazine Article Titles
                magazine = select_magazine(magazines)
                if not magazine:
                    continue
                articles = magazine.articles()
                if not articles:
                    print(f"No articles found for magazine '{magazine.name}'.")
                else:
                    print(f"Articles in magazine '{magazine.name}':")
                    for art in articles:
                        print(f"- {art.title}")

            elif choice == '7':  # Show Magazine Contributors
                magazine = select_magazine(magazines)
                if not magazine:
                    continue
                contributors = magazine.contributors()
                if not contributors:
                    print(f"No contributors found for magazine '{magazine.name}'.")
                else:
                    print(f"Contributors for '{magazine.name}':")
                    for author in contributors:
                        print(f"- {author.name}")

            elif choice == '8':  # Show Magazine Contributing Authors (>2 articles)
                magazine = select_magazine(magazines)
                if not magazine:
                    continue
                top_authors = magazine.contributing_authors()
                if not top_authors:
                    print(f"No contributing authors with >2 articles found for '{magazine.name}'.")
                else:
                    print(f"Top contributing authors for '{magazine.name}':")
                    for author in top_authors:
                        print(f"- {author.name}")

            elif choice == '9':  # Show Author's Topic Areas
                author = select_author(authors)
                if not author:
                    continue
                topics = author.topic_areas()
                if not topics:
                    print(f"No topic areas found for author '{author.name}'.")
                else:
                    print(f"Topic areas for {author.name}:")
                    for topic in topics:
                        print(f"- {topic}")

            elif choice == '0':
                print("Exiting the Articles App. Goodbye!")
                break

            else:
                print("Invalid choice, please select a valid option.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
