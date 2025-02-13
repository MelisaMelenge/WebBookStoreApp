from typing import Optional
from fastapi import APIRouter, HTTPException
from services.shoppingcart_services import ShoppingCartServices
from repositories.shoppingcart import ShoppingCart
from repositories.book import BookDAO

router = APIRouter()
services = ShoppingCartServices()

@router.post("/shoppingcart/create")
def create_cart(user_id: int) -> ShoppingCart:
    """Endpoint to create a new shopping cart for a user
    
    Args:
        user_id (int): ID of the user who owns the cart
    
    Returns:
        ShoppingCart: Created instance of ShoppingCart
    """
    try:
        return services.create_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/shoppingcart/add_item")
def add_item_to_cart(user_id: int, book: BookDAO, quantity: int = 1) -> Optional[ShoppingCart]:
    """Endpoint to add an item to the user's shopping cart
    
    Args:
        user_id (int): ID of the user who owns the cart
        book (BookDAO): Book object to add
        quantity (int): Quantity of the book to add. Default is 1
    
    Returns:
        Optional[ShoppingCart]: Updated cart or None if not found
    """
    try:
        return services.add_item_to_cart(user_id, book, quantity)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/shoppingcart/remove_item")
def remove_item_from_cart(user_id: int, isbn: str) -> Optional[ShoppingCart]:
    """Endpoint to remove an item from the user's shopping cart
    
    Args:
        user_id (int): ID of the user who owns the cart
        isbn (str): ISBN of the book to remove
    
    Returns:
        Optional[ShoppingCart]: Updated cart or None if not found
    """
    try:
        return services.remove_item_from_cart(user_id, isbn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/shoppingcart/{user_id}", response_model=Optional[ShoppingCart])
def find_cart_by_user_id(user_id: int) -> Optional[ShoppingCart]:
    """Endpoint to find a shopping cart by the user's ID
    
    Args:
        user_id (int): ID of the user who owns the cart
    
    Returns:
        Optional[ShoppingCart]: Found cart or None if it does not exist
    """
    try:
        return services.find_cart_by_user_id(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/shoppingcart/show/{user_id}", response_model=Optional[str])
def show_cart(user_id: int) -> Optional[str]:
    """Endpoint to show the content of the user's shopping cart
    
    Args:
        user_id (int): ID of the user who owns the cart
    
    Returns:
        Optional[str]: String representation of the cart or None if not found
    """
    try:
        return services.show_cart(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))