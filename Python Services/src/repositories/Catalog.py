"""This module is used to handle data related to the catalog and books.

Author: Cristian Gamez <cristiangameznunez@gmail.com>"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .book import BookRepository, BookDAO

# strategy pattern
class SearchStrategy(ABC):
    """SearchStrategy class to represent a search strategy object"""
    @abstractmethod
    def search(self, criteria: str) -> List[str]:
        """This method is used to search for books based on a criteria"""
        pass


class SearchByAuthor(SearchStrategy):
    """SearchByAuthor class to represent a search by author object"""
    def __init__(self, books: List[BookDAO]):
        self.books = books  # Lista de objetos Book
        
    def search(self, criteria: str) -> List[str]:
        """This method is used to search for books based on author"""
        return [book.title for book in self.books if criteria.lower() in book.author.lower()]

class SearchByISBN(SearchStrategy):
    """SearchByISBN class to represent a search by ISBN object"""
    def __init__(self, books: List[BookDAO]):
        self.books = books  # Debe ser una lista de objetos Book
        
    def search(self, criteria: str) -> List[str]:
        """This method is used to search for books based on ISBN"""
        return [book.title for book in self.books if criteria in book.isbn]


class SearchByTitle(SearchStrategy):
    """SearchByTitle class to represent a search by title object"""
    def __init__(self, books: List[BookDAO]):
        self.books = books
        
    def search(self, criteria: str) -> List[str]:
        """This method is used to search for books based on title"""
        return [book.title for book in self.books if criteria.lower() in book.title.lower()]


class Catalog:
    """Catalog class to represent a catalog object"""
    _instance = None
    
    # Singleton pattern
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Catalog, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """Method to initialize the catalog"""
        self.__books = []
        self.add_books_catalog()
        self.search_strategy: Optional[SearchStrategy] = None 
    
    def add_books_catalog(self):
        """Method to add books to the catalog"""
        book_repository = BookRepository()  
        books = book_repository.get_books()
        for book in books:
            self.__books.append(BookDAO(title=book.title, author=book.author, isbn=book.isbn, price=book.price, description=book.description, category=book.category, stock=book.stock))
    
    def get_books(self):
        """Method to get books from the catalog using the current search strategy"""
        return self.__books
    
    def set_search_strategy(self, strategy: SearchStrategy):
        """Set a new search strategy"""
        self.search_strategy = strategy

    def get_books_for_author(self, author: str) -> List[str]:
        """Method to get books by author"""
        self.set_search_strategy(SearchByAuthor(self.__books))
        return self.search_strategy.search(author)

    def get_books_for_isbn(self, isbn: str) -> List[str]:
        """Method to get books by ISBN"""
        self.set_search_strategy(SearchByISBN(self.__books))
        return self.search_strategy.search(isbn)

    def get_books_for_title(self, title: str) -> List[str]:
        """Method to get books by title"""
        self.set_search_strategy(SearchByTitle(self.__books))
        return self.search_strategy.search(title)

        