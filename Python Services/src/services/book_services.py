"""This module is used to provide services related to books.

Author: Cristian Gamez <cristiangameznunez@gmail.com>"""
import sys
import os

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from repositories.book import BookRepository, BookDAO
from typing import List

class BookServices:
    """This class provides services to handle books in the application"""

    def __init__(self):
        self.book_repository = BookRepository()

    def get_all_books(self) -> List[BookDAO]:
        """Service to get all books
        
        Returns:
            List[BookDAO]: A list of BookDAO objects representing all books
        """
        return self.book_repository.get_books()