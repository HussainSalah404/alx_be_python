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