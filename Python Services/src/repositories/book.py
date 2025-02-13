"""This module is used to handle data related to videogames.

Author: Cristian Gamez <cristiangameznunez@gmail.com>"""


from pydantic import BaseModel
from .environment_variables import EnvironmentVariables
from typing import List
import json


class BookDAO(BaseModel):
    """ BookDAO class to handle data related to books """
    title: str
    author: str
    isbn: str
    price: float
    description: str
    category: str
    stock: int

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, price={self.price}, description={self.description}, category={self.category}, stock={self.stock})"
    
# Factory pattern
class BookFactory:
    """ BookFactory class to create a book object """
    @staticmethod
    def create_book(title, author, isbn, price, description, category, stock):
        """ Method to create a book object from the given arguments
        args:
            title: str
            author: str
            isbn: str
            price: float
            description: str
            category: str
            stock: int
        return:
            Book object
        """
        book=BookDAO(title=title, author=author, isbn=isbn, price=price, description=description, category=category, stock=stock)
        
        return book
    
class BookRepository:
    """This class represents the behavior os a repository to handle books in the application"""
    
    def __init__(self):
        env = EnvironmentVariables()
        path_books_data = env.path_books_data
        self._load_data(path_books_data)
    
    def _load_data(self, path_file: str):
        """ Method to load data from a file """
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception as e:
            print(f"ERROR. Could not load data from file: {e}")
            self.data = []
    
    def get_books(self) -> List[BookDAO]:
        """ Method to get all books """
        catalog = []
        for book in self.data:
            book_obj = BookFactory.create_book(
                title=book["title"],
                author=book["author"],
                isbn=book["isbn"],
                price=book["price"],
                description=book["description"],
                category=book["category"],
                stock=book["stock"]
            )
            catalog.append(book_obj)
        return catalog


