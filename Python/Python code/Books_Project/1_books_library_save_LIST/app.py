from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Choise > """


def menu():
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


def prompt_add_book():  # Pratar med utils.database.py
    name = input('Book name: ')
    author = input('Book author: ')
    return database.add_book(name, author)


def list_books():
    for i, book in enumerate(database.books):
        print((f'{i + 1}.\n Name:   {book["name"]}\n'
               f' Author: {book["author"]}\n'
               f' Read:   {"Yes" if book["read"] else "No"}'))


def prompt_read_book():
    name = input('Mark book as read\n'
                 'Bookname: ')
    database.add_book()


def prompt_delete_book():
    name = input('DELETE BOOK!\nBook name: ')
    database.delete_book(name)
    list_books()

menu()
