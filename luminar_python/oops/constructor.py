# CONSTRUCTOR
# constructor initialises instance variable.
# constructor can be used as __init__().
# instead of calling the create() method, we can use the constructor.

class Book():
    book_name:str
    author:str
    genre:str
    price:int
    pages:int

    def __init__(self,book_name,author,genre,price,pages):
        self.book_name=book_name
        self.author=author
        self.genre=genre
        self.price=price
        self.pages=pages

    def get(self):
        print(self.book_name,self.author,self.price)

    def __str__(self):                                # to represent the string values.
        return self.author
obj=Book("heart bones","collen hoover","romance",250,400)
print(obj.book_name)
print(obj)


 