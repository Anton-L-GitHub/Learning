from utils import database

USER_CHOICE = """
Enter:
- 'a' - to add a new book
- 'l' - to list all the books
- 'r' - to mark a book as read
- 'd' - to delete a book
- 'q' - to quit

Choise > """


def menu():
    database.create_book_table()
    user_inpuit = input(USER_CHOICE)
    while user_inpuit != 'q':
        if user_inpuit == 'a':
            prompt_add_book()
        elif user_inpuit == 'l':
            list_books()
        elif user_inpuit == 'r':
            prompt_read_book()
        elif user_inpuit == 'd':
            prompt_delete_book()

        user_inpuit = input(USER_CHOICE)


def prompt_add_book():
    name = input('Book name: ')
    author = input('Book author: ')
    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for i, book in enumerate(books):
        print(f'B{i + 1}\n Namn: {book["name"]}\n Author: {book["author"]}\n Read: {"Yes" if book["read"] else "Nope"}')


def prompt_read_book():
    name = input('Book name: ')
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input('DELETE BOOK!\nBook name: ')
    database.delete_book(name)


menu()
