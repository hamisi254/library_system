import json
from datetime import datetime


class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.borrow_count = 0  # For tracking most borrowed book

    def display_info(self):
        return f"Book ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Available: {self.available_copies}"

    def update_copies(self, number):
        self.available_copies += number
        if self.available_copies < 0:
            self.available_copies = 0

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available_copies": self.available_copies,
            "borrow_count": self.borrow_count
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(data["book_id"], data["title"], data["author"], data["available_copies"])
        book.borrow_count = data.get("borrow_count", 0)
        return book


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # List of book titles

    def borrow_book(self, book):
        if book.available_copies > 0:
            self.borrowed_books.append(book.title)
            book.update_copies(-1)
            book.borrow_count += 1
            return True
        return False

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            return True
        return False

    def display_member_info(self):
        borrowed = ', '.join(self.borrowed_books) if self.borrowed_books else "None"
        return f"Member ID: {self.member_id} | Name: {self.name} | Borrowed Books: {borrowed}"

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        member = cls(data["member_id"], data["name"])
        member.borrowed_books = data.get("borrowed_books", [])
        return member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        for book in self.books:
            print(book.display_info())

    def display_all_members(self):
        if not self.members:
            print("No members registered.")
        for member in self.members:
            print(member.display_member_info())

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_transaction(self, member_id, book_title):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_title(book_title)
        if not member:
            return "Member not found."
        if not book:
            return "Book not found."
        if book.available_copies <= 0:
            return "Book is not available for borrowing."
        if book.title in member.borrowed_books:
            return "Member has already borrowed this book."
        if member.borrow_book(book):
            # Log transaction
            with open("transactions.txt", "a") as f:
                f.write(f"{datetime.now()} | BORROW | Member: {member_id} | Book: {book_title}\n")
            return "Book borrowed successfully!"
        return "Failed to borrow book."

    def return_transaction(self, member_id, book_title):
        member = self.find_member_by_id(member_id)
        if not member:
            return "Member not found."
        if book_title not in member.borrowed_books:
            return "This book was not borrowed by the member."
        book = self.find_book_by_title(book_title)
        if book:
            book.update_copies(1)
        member.return_book(book_title)
        # Log transaction
        with open("transactions.txt", "a") as f:
            f.write(f"{datetime.now()} | RETURN | Member: {member_id} | Book: {book_title}\n")
        return "Book returned successfully!"

    def most_borrowed_book(self):
        if not self.books:
            return "No books available."
        most_borrowed = max(self.books, key=lambda b: b.borrow_count)
        if most_borrowed.borrow_count == 0:
            return "No books have been borrowed yet."
        return f"Most borrowed book: '{most_borrowed.title}' by {most_borrowed.author} (Borrowed {most_borrowed.borrow_count} times)"

    def search_books_by_author(self, author):
        results = [book for book in self.books if author.lower() in book.author.lower()]
        if not results:
            print("No books found by that author.")
        else:
            for book in results:
                print(book.display_info())

    # Save and load methods
    def save_data(self):
        with open("books.txt", "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)
        with open("members.txt", "w") as f:
            json.dump([member.to_dict() for member in self.members], f, indent=2)

    def load_data(self):
        try:
            with open("books.txt", "r") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(b) for b in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

        try:
            with open("members.txt", "r") as f:
                members_data = json.load(f)
                self.members = [Member.from_dict(m) for m in members_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.members = []