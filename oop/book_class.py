class Book:
    def __init__(self, title, author, year):
        """Initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string format for users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"