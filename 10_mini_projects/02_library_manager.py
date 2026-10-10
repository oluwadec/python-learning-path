"""02_library_manager.py - Mini project: borrow and return books."""


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.borrowed_by = None

    def __str__(self) -> str:
        status = f"borrowed by {self.borrowed_by}" if self.borrowed_by else "available"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add(self, book: Book) -> None:
        self.books.append(book)

    def find(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow(self, title: str, member: str) -> str:
        book = self.find(title)
        if book is None:
            return f"'{title}' is not in the library"
        if book.borrowed_by:
            return f"'{title}' is already borrowed"
        book.borrowed_by = member
        return f"{member} borrowed '{book.title}'"

    def give_back(self, title: str) -> str:
        book = self.find(title)
        if book and book.borrowed_by:
            book.borrowed_by = None
            return f"'{book.title}' returned"
        return "Nothing to return"


if __name__ == "__main__":
    library = Library()
    library.add(Book("Dune", "Frank Herbert"))
    library.add(Book("Emma", "Jane Austen"))

    print(library.borrow("dune", "Ada"))
    print(library.borrow("Dune", "Ben"))
    print(library.borrow("Hamlet", "Ben"))
    print(library.give_back("Dune"))
    for book in library.books:
        print(book)
