class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def __str__(self):
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"{self.title} by {self.author} - ({status})"
    
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

book1.check_out()
book2.return_book()
book3.check_out()
book3.return_book()

print(book1)
print(book2)
print(book3)