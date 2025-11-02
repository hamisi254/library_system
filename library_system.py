from models import Library, Book, Member
import time

def show_loading_dots(message="Processing", dots=5, delay=0.3):
    print(f"{message}", end="", flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

def show_welcome_page():
    ascii_art = r"""
███    ███  ██████  ██████  ███████ ███████ ████████ 
████  ████ ██    ██ ██   ██ ██      ██         ██    
██ ████ ██ ██    ██ ██████  █████   █████      ██    
██  ██  ██ ██    ██ ██   ██ ██      ██         ██    
██      ██  ██████  ██   ██ ███████ ███████    ██    
"""
    print(ascii_art)
    print("          M O B  L I B R A R Y  S Y S T E M")
    print("    📚  Smart Library Management System  📚")
    print("\n    Managing books, members, and transactions made easy!")
    print("    Developed with Python OOP • Persistent Data Storage\n")
    print("    Initializing system", end="", flush=True)
    for _ in range(4):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(1)

def main():
    show_welcome_page()
    library = Library()
    library.load_data()  # Load existing data on startup

    while True:
        print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Add New Member")
        print("3. Display All Books")
        print("4. Display All Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Most Borrowed Book")
        print("8. Search Books by Author")
        print("9. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            try:
                copies = int(input("Enter Available Copies: "))
                if copies < 0:
                    raise ValueError
                book = Book(book_id, title, author, copies)
                library.add_book(book)
                library.save_data()
                show_loading_dots("Adding book", dots=4, delay=0.5)
                print("Book added successfully!")
            except ValueError:
                show_loading_dots("Adding book", dots=4, delay=0.25)
                print("Invalid input for copies. Must be a non-negative integer.")

        elif choice == '2':
            member_id = input("Enter Member ID: ").strip()
            name = input("Enter Name: ").strip()
            member = Member(member_id, name)
            library.add_member(member)
            library.save_data()
            show_loading_dots("Adding member", dots=4, delay=0.5)
            print("Member added successfully!")

        elif choice == '3':
            library.display_all_books()

        elif choice == '4':
            library.display_all_members()

        elif choice == '5':
            mid = input("Enter Member ID: ").strip()
            title = input("Enter Book Title: ").strip()
            msg = library.borrow_transaction(mid, title)
            show_loading_dots("Borrowing book", dots=4, delay=0.5)
            print(msg)

        elif choice == '6':
            mid = input("Enter Member ID: ").strip()
            member = library.find_member_by_id(mid)
            if not member:
                show_loading_dots("", dots=4, delay=0.25)
                print("Member not found.")
                continue

            if not member.borrowed_books:
                show_loading_dots("", dots=4, delay=0.25)
                print(f"{member.name} has no books to return.")
                continue

            print(f"\nBooks borrowed by {member.name}:")
            for idx, book_title in enumerate(member.borrowed_books, 1):
                print(f"{idx}. {book_title}")

            print("\nEnter the number of the book to return, or type the exact book title:")
            user_input = input("Your choice: ").strip()

            title = None
            if user_input.isdigit():
                choice_num = int(user_input)
                if 1 <= choice_num <= len(member.borrowed_books):
                    title = member.borrowed_books[choice_num - 1]
                else:
                    show_loading_dots("", dots=4, delay=0.25)
                    print("Invalid number selected.")
                    continue
            else:
                if user_input in member.borrowed_books:
                    title = user_input
                else:
                    show_loading_dots("Borrowing book", dots=4, delay=0.25)
                    print("You haven't borrowed a book with that title. Please check the list above.")
                    continue

            msg = library.return_transaction(mid, title)
            show_loading_dots("Returning book", dots=4, delay=0.5)
            print(msg)

        elif choice == '7':
            show_loading_dots("", dots=4, delay=0.25)
            print(library.most_borrowed_book())

        elif choice == '8':
            author = input("Enter Author Name: ").strip()
            show_loading_dots("searching", dots=4, delay=0.5)
            library.search_books_by_author(author)

        elif choice == '9':
            library.save_data()
            print("Thank you for using the Smart Library System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()