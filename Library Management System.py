import json
from datetime import datetime, timedelta


# -------------------- Book Class --------------------
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }


# -------------------- Library Class --------------------
class Library:
    def __init__(self, filename="library_data.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return {bid: Book(**info) for bid, info in data.items()}
        except FileNotFoundError:
            return {}

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(
                {bid: book.to_dict() for bid, book in self.books.items()},
                file,
                indent=4
            )

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("❌ Book ID already exists.")
            return
        self.books[book_id] = Book(book_id, title, author)
        self.save_books()
        print("✅ Book added successfully.")

    def view_books(self):
        if not self.books:
            print("📚 No books available.")
            return
        print("\n--- Library Books ---")
        for book in self.books.values():
            status = "Available" if book.available else "Issued"
            print(f"{book.book_id} | {book.title} | {book.author} | {status}")

    def issue_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("❌ Book not found.")
        elif not book.available:
            print("❌ Book already issued.")
        else:
            book.available = False
            self.save_books()
            print("📖 Book issued successfully.")

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            print("❌ Book not found.")
        elif book.available:
            print("❌ Book was not issued.")
        else:
            book.available = True
            self.save_books()
            print("✅ Book returned successfully.")


# -------------------- Menu Function --------------------
def main():
    library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.view_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("👋 Exiting Library System.")
            break

        else:
            print("❌ Invalid choice. Try again.")


# -------------------- Run Program --------------------
if __name__ == "__main__":
    main()
