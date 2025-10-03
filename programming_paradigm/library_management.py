# programming_paradigm/library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title              # public attribute
        self.author = author            # public attribute
        self._is_checked_out = False    # private attribute

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """A class representing a library containing books."""

    def __init__(self):
        self._books = []   # private list of Book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}' successfully.")
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title if it exists in the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}' successfully.")
                return
        print(f"'{title}' was not checked out from this library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
