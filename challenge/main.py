from interfaces.book import Book

from book_collection import BookCollection
from fiction_book import FictionBook
from nonfiction_book import NonFictionBook


def library_checkout(book: Book):
    print("Checkout process begins")
    book.checkout()
    print("Checkout process ends\n")

def library_return(book: Book):
    print("Return process begins")
    book.return_book()
    print("Return process ends\n")    

fb_1: FictionBook = FictionBook("FictionBook1")
nfb_1: NonFictionBook = NonFictionBook("NonFictionBook1")
nfb_2: NonFictionBook = NonFictionBook("NonFictionBook2")

book_collection: BookCollection = BookCollection()
book_collection.add_book(fb_1)
book_collection.add_book(nfb_1)
book_collection.add_book(nfb_2)


library_checkout(fb_1)
library_checkout(fb_1)
library_return(fb_1)
library_return(nfb_2)
library_checkout(fb_1)

library_checkout(book_collection)
library_return(book_collection)