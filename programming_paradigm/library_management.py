class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self) -> bool:
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True
    
    def return_book(self) -> bool:
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True
    
    def is_available(self) -> bool:
        return not self._is_checked_out
    
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book) -> None:
        self._books.append(book)
    
    def check_out_book(self, title: str) -> bool:
        book = self._find_book(title)
        if book and book.is_available():
            return book.check_out()
        return False
    
    def return_book(self, title: str) -> bool:
        book = self._find_book(title)
        if book:
            return book.return_book()
        return False
    
    def list_available_books(self) -> None:
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(str(book))
    
    def _find_book(self, title: str) -> Book | None:
        for book in self._books:
            if book.title == title:
                return book
        return None