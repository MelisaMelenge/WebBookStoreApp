import os
from dotenv import load_dotenv

import sys

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()


class EnvironmentVariables:
    """This class is used to handle environment variables."""

    def __init__(self):
        """This method is used to initialize the class."""
        self.path_books_data = os.getenv('PATH_BOOKS_DATA')