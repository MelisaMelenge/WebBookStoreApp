from pydantic import BaseModel
from typing import List, Optional
from .book import BookDAO


class ShoppingCartItem(BaseModel):
    """
    Class representing an item in the shopping cart.
    Contains information about a book and the selected quantity.
    """
    book: BookDAO  # Book object
    quantity: int  # Quantity of the book in the cart

    def __str__(self) -> str:
        """
        String representation of the item.
        """
        return f"ShoppingCartItem(book={self.book}, quantity={self.quantity})"


# ShoppingCart class (Data Model)
class ShoppingCart(BaseModel):
    """
    Class representing the shopping cart.
    Contains attributes related to the items in the cart.
    """
    user_id: int  # ID of the user who owns the cart
    items: List[ShoppingCartItem] = []  # List of items in the cart

    def __str__(self) -> str:
        """
        String representation of the cart.
        """
        items_str = ", ".join([str(item) for item in self.items])
        return f"ShoppingCart(user_id={self.user_id}, items=[{items_str}])"


# ShoppingCartRepository class (Behaviors)
class ShoppingCartRepository:
    """
    Class handling the behaviors (methods) related to the shopping cart.
    """
    def __init__(self):
        """
        Constructor of the ShoppingCartRepository class.
        Initializes an empty list to store the carts.
        """
        self.carts: List[ShoppingCart] = []

    def create_cart(self, user_id: int) -> ShoppingCart:
        """
        Creates a new shopping cart for a user.

        :param user_id: ID of the user who owns the cart (int).
        :return: Created instance of ShoppingCart.
        """
        cart = ShoppingCart(user_id=user_id)
        self.carts.append(cart)
        return cart

    def add_item_to_cart(self, user_id: int, book: BookDAO, quantity: int = 1) -> Optional[ShoppingCart]:
        """
        Adds an item to the user's shopping cart.

        :param user_id: ID of the user who owns the cart (int).
        :param book: Book object to add (BookDAO).
        :param quantity: Quantity of the book to add (int). Default is 1.
        :return: Updated cart or None if not found.
        """
        cart = self.find_cart_by_user_id(user_id)
        if cart:
            # Check if the item already exists in the cart
            item_exists = False
            for item in cart.items:
                if item.book.isbn == book.isbn:
                    item.quantity += quantity  # Increment the quantity if it already exists
                    item_exists = True
                    break
            if not item_exists:
                # Add a new item if it does not exist
                cart.items.append(ShoppingCartItem(book=book, quantity=quantity))
            return cart
        return None

    def remove_item_from_cart(self, user_id: int, isbn: str) -> Optional[ShoppingCart]:
        """
        Removes an item from the user's shopping cart.

        :param user_id: ID of the user who owns the cart (int).
        :param isbn: ISBN of the book to remove (str).
        :return: Updated cart or None if not found.
        """
        cart = self.find_cart_by_user_id(user_id)
        if cart:
            # Find and remove the item
            cart.items = [item for item in cart.items if item.book.isbn != isbn]
            return cart
        return None

    def find_cart_by_user_id(self, user_id: int) -> Optional[ShoppingCart]:
        """
        Finds a shopping cart by the user's ID.

        :param user_id: ID of the user who owns the cart (int).
        :return: Found cart or None if it does not exist.
        """
        for cart in self.carts:
            if cart.user_id == user_id:
                return cart
        return None

    def show_cart(self, user_id: int) -> Optional[str]:
        """
        Shows the content of the user's shopping cart.

        :param user_id: ID of the user who owns the cart (int).
        :return: String representation of the cart or None if not found.
        """
        cart = self.find_cart_by_user_id(user_id)
        return str(cart) if cart else None


