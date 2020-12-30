from interfaces.book import Book

class BookCollection(Book):
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book):
        self.books.append(book)

    def checkout(self):
        [b.checkout() for b in self.books]

    def return_book(self):
        [b.return_book() for b in self.books]
