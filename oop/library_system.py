class Book:
    """
    base class representing a book with title and author
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
class EBook(Book):
    """
    this class reps objects passed as softcopy books
    it inheris the parent class attributes
    """
    def __init__(self, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """
    this class represents a physical book
    it inherits from the parent class Book
    """
    def __init__(self, page_count: int):
        #calling the base class __init__ method whose attributes are needed for         each instance
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    this class represents a collection of books passed as either
    Printbook, Ebook, or Book
    """
    def __init__(self):
        #initialising a list
        self.books = []
    
    def add_book(self, book):
        """
        adds a Book, EBook, or Printbook instance to the library collection
        the book attribute doesnt need to renew each time we create new instance
        we need book to be passed to the empty list we just created
        """
        return self.books.append(book)
    
    def list_books(self):
        """
        displays all books in the library 
        """
        if not self.books:
            print("The library is empty.")
        else:
            for books in self.books:
                #we have to check instance type and declare it
                if isinstance(book, Ebook):
                    print(f"Ebook: {self.title} by {self.author}")
                elif isinstance(book, PrintBook):
                    print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")

                else:
                    print(f"Book: {self.title} by {self.author})
