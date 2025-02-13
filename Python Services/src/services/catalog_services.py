"""This module is used to provide services related to the catalog and books.

Author: Cristian Gamez <cristiangameznunez@gmail.com>"""

import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.Catalog import Catalog, SearchStrategy
from typing import List
class CatalogServices:
    """This class provides services to handle the catalog in the application"""

    def __init__(self):
        self.catalog = Catalog()

    def initialize_catalog(self):
        """Service to initialize the catalog
        
        Returns:
            None
        """
        self.catalog.initialize()

    def add_books_to_catalog(self):
        """Service to add books to the catalog
        
        Returns:
            None
        """
        self.catalog.add_books_catalog()

    def get_all_books(self) -> List:
        """Service to get all books from the catalog
        
        Returns:
            List: A list of BookDAO objects representing all books in the catalog
        """
        return self.catalog.get_books()

    def set_search_strategy(self, strategy: SearchStrategy):
        """Service to set a new search strategy
        
        Args:
            strategy (SearchStrategy): The search strategy to be set
        
        Returns:
            None
        """
        self.catalog.set_search_strategy(strategy)

    def get_books_by_author(self, author: str) -> List[str]:
        """Service to get books by author
        
        Args:
            author (str): The author to search for
        
        Returns:
            List[str]: A list of book titles by the specified author
        """
        return self.catalog.get_books_for_author(author)

    def get_books_by_isbn(self, isbn: str) -> List[str]:
        """Service to get books by ISBN
        
        Args:
            isbn (str): The ISBN to search for
        
        Returns:
            List[str]: A list of book titles with the specified ISBN
        """
        return self.catalog.get_books_for_isbn(isbn)

    def get_books_by_title(self, title: str) -> List[str]:
        """Service to get books by title
        
        Args:
            title (str): The title to search for
        
        Returns:
            List[str]: A list of book titles with the specified title
        """
        return self.catalog.get_books_for_title(title)