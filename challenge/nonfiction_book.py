from interfaces.book import Book

class NonFictionBook(Book):
    def __init__(self, name):
        self.name = name
        self.checked_out = False

    def checkout(self):
        if not self.checked_out:
            print("Checking out {}\n".format(self.name))
            self.checked_out = True
        else:
            print("{} is already checked out\n".format(self.name))
    
    def return_book(self):
        if self.checked_out:
            print("Returning {}\n".format(self.name))
            self.checked_out = False
        else:
            print("{} is not checked out\n".format(self.name))

    