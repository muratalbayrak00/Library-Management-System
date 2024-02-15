class Book:
    def __init__(self, title, author, year, number_of_pages):
        self.title = title
        self.author = author
        self.year = year
        self.number_of_pages = number_of_pages
    def str(self):
        book_info = f"{self.title},{self.author},{self.year},{self.number_of_pages}\n"
        return book_info

    def list_books(self):
        book_info = f"Book: {self.title}, Author: {self.author}\n"
        return book_info


