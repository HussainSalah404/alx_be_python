class Book:
    def __init__(self, title, author):
        self.title = title            # public
        self.author = author          # public
        self._is_checked_out = False  # private (by convention)

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f'"{self.title}" has been checked out.')
        else:
            print(f'"{self.title}" is already checked out.')

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            print(f'"{self.title}" has been returned.')
        else:
            print(f'"{self.title}" was not checked out.')

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        self._books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f'You have checked out "{book.title}".')
                return
        print(f'"{title}" is not available for checkout.')

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f'You have returned "{book.title}".')
                return
        print(f'"{title}" is not currently checked out.')

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available:
                print(f'- {book.title} by {book.author}')