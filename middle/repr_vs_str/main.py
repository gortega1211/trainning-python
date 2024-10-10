from datetime import datetime

today = datetime.now()
print(repr(today)) # __repr__
print(today) # __str__

print(format(today)) # __str__
print("{}".format(today)) # __str__
print(f"{today}") # __str__
print(f"{today!r}") # __repr__
print(f"{today = }") # __repr__
print(f"{today = !s}") # __str__

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(title={self.title!r}, author={self.author!r})"

    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
book = Book("The Oddysey", "Homer")
print(repr(book))
print(str(book))