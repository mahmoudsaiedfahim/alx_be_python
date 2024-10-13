'''this script, define a Book class that uses specific 
magic methods to enhance its functionality. 
This class will model a book with attributes for the title, 
author, and publication year.'''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting '{self.title}'")

    def __str__(self):#string representation
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):#official representation
        return f"Book('{self.title}', '{self.author}', {self.year})"
