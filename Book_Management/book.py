import csv


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} in {self.year}"


class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            print("A book with this title already exists")

    def display_books(self):
        if not self.books:
            print("No books in the collection.")
            return
        print("\nBooks in the collection:")
        headers = ["Title", "Author", "Year"]
        print(f"{headers[0]:<30}{headers[1]:<30}{headers[2]:<10}")
        print("-" * 70)
        for book in self.books:
            print(f"{book.title:<30}{book.author:<30}{book.year:<10}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def remove_book(self, title):
        book = self.search_book(title)
        if book:
            self.books.remove(book)
            return True
        return False

    def update_book(self, title, new_title, new_author, new_year):
        book = self.search_book(title)
        if book:
            book.title = new_title
            book.author = new_author
            book.year = new_year
            return True
        return False

    def save_books(self, filename):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Author", "Year"])
                for book in self.books:
                    writer.writerow([book.title, book.author, book.year])
            print(f"Books saved successfully to {filename}")
        except Exception as e:
            print(f"An error occurred while saving books: {e}")

    def load_books(self, filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if len(row) == 3:
                        title, author, year = row
                        book = Book(title, author, year)
                        self.add_book(book)
            print(f"Books loaded from {filename}.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"An error occurred while loading books: {e}")


def get_valid_year():
    while True:
        year = input("Enter the year of publication: ")
        if year.isdigit() and int(year) > 0:
            return year
        print("Invalid year")
