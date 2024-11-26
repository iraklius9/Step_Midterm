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
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the collection.")
            return
        for book in self.books:
            print(book)

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
        with open(filename, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")

    def load_books(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line or len(line.split(',')) != 3:
                        continue
                    title, author, year = line.split(',')

                    book = Book(title, author, year)
                    self.add_book(book)
        except FileNotFoundError:
            print(f"File '{filename}' not found")


def get_valid_year(num):
    while True:
        year = input(num)
        if year.isdigit() and int(year) > 0:
            return year
        print("Invalid year")
