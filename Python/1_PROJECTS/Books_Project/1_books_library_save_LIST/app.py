from utils import database

USER_CHOICE = """Ange..
    '1' - Lägg till bok
    '2' - Se alla böcker
    '3' -
    '4' to delete a book

    '0' - Avsluta
    Choise > """


def menu():
    user_inpuit = input(USER_CHOICE)
    while user_inpuit != '0':
        if user_inpuit == '1':
            prompt_add_book()
        elif user_inpuit == '2':
            list_books()
        elif user_inpuit == '3':
            prompt_read_book()
        elif user_inpuit == '4':
            prompt_delete_book()
        user_inpuit = input(USER_CHOICE)


def prompt_add_book():
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
