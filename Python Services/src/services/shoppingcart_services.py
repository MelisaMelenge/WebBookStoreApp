"""This module is used to provide services related to the shopping cart.

Author: Cristian Gamez <cristiangameznunez@gmail.com>"""

from repositories.shoppingcart import ShoppingCartRepository, ShoppingCart
from repositories.book import BookDAO
from typing import Optional

class ShoppingCartServices:
    """This class provides services to handle the shopping cart in the application"""

    def __init__(self):
        self.shopping_cart_repository = ShoppingCartRepository()

    def create_cart(self, user_id: int) -> ShoppingCart:
        """Service to create a new shopping cart for a user
        
        Args:
            user_id (int): ID of the user who owns the cart
        
        Returns:
            ShoppingCart: Created instance of ShoppingCart
        """
        return self.shopping_cart_repository.create_cart(user_id)

    def add_item_to_cart(self, user_id: int, book: BookDAO, quantity: int = 1) -> Optional[ShoppingCart]:
        """Service to add an item to the user's shopping cart
        
        Args:
            user_id (int): ID of the user who owns the cart
            book (BookDAO): Book object to add
            quantity (int): Quantity of the book to add. Default is 1
        
        Returns:
            Optional[ShoppingCart]: Updated cart or None if not found
        """
        return self.shopping_cart_repository.add_item_to_cart(user_id, book, quantity)

    def remove_item_from_cart(self, user_id: int, isbn: str) -> Optional[ShoppingCart]:
        """Service to remove an item from the user's shopping cart
        
        Args:
            user_id (int): ID of the user who owns the cart
            isbn (str): ISBN of the book to remove
        
        Returns:
            Optional[ShoppingCart]: Updated cart or None if not found
        """
        return self.shopping_cart_repository.remove_item_from_cart(user_id, isbn)

    def find_cart_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        """Service to find a shopping cart by the user's ID
        
        Args:
            user_id (int): ID of the user who owns the cart
        
        Returns:
            Optional[ShoppingCart]: Found cart or None if it does not exist
        """
        return self.shopping_cart_repository.find_cart_by_user_id(user_id)

    def show_cart(self, user_id: int) -> Optional[str]:
        """Service to show the content of the user's shopping cart
        
        Args:
            user_id (int): ID of the user who owns the cart
        
        Returns:
            Optional[str]: String representation of the cart or None if not found
        """
        return self.shopping_cart_repository.show_cart(user_id)