class Book:
    def __init__(self, title, author, __is_checked_out):
        self.title = title
        self.author = author
        self.__is_checked_out = __is_checked_out

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self):
        self.__books.append(new_book)

    def check_out_book(self, title):
        self.__books.remove(title)

    def return_book(self, title):
        self.__books.add(title)
        return True

    def list_available_books(self):
        print(self.__books)

