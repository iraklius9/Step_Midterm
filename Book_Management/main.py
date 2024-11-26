from book import *


def main():
    manager = BookManager()
    manager.load_books("books.txt")

    while True:
        print("\nBook Manager")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Update Book")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            if manager.search_book(title):
                print("A book with this title already exists.")
                continue

            author = input("Enter the author: ").strip()
            if not author:
                print("Author cannot be empty.")
                continue

            year = get_valid_year("Enter the year of publication: ")
            manager.add_book(Book(title, author, year))
            print("Book added successfully.")

        elif choice == "2":
            manager.display_books()

        elif choice == "3":
            title = input("Enter the title of the book: ").strip()
            book = manager.search_book(title)
            if book:
                print("Book found:", book)
            else:
                print("Book not found.")

        elif choice == "4":
            title = input("Enter the title of the book to remove: ").strip()
            if manager.remove_book(title):
                print("Book removed successfully.")
            else:
                print("Book not found.")

        elif choice == "5":
            title = input("Enter the title of the book to update: ").strip()
            if not manager.search_book(title):
                print("Book not found.")
                continue

            new_title = input("Enter the new title: ").strip()
            if not new_title:
                print("Title cannot be empty.")
                continue

            new_author = input("Enter the new author: ").strip()
            if not new_author:
                print("Author cannot be empty.")
                continue

            new_year = get_valid_year("Enter the new year of publication: ")
            manager.update_book(title, new_title, new_author, new_year)
            print("Book updated successfully.")

        elif choice == "6":
            manager.save_books("books.txt")
            print("Books saved. Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()
