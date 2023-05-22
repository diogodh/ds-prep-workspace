class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        a = "Title: " + self.title + ", Author: " + self.author + ", Price: " + str(self.price)
        return a

def get_total_price(books):
    total_price = 0.0
    for book in books:
        total_price += book[2]
    return total_price


description = "this is a module named bookstore"