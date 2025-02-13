from typing import List
from fastapi import APIRouter, HTTPException
from services.catalog_services import CatalogServices
from repositories.book import BookDAO
from repositories.Catalog import SearchStrategy
from repositories.Catalog import SearchByAuthor, SearchByISBN, SearchByTitle

router = APIRouter()
services = CatalogServices()

@router.post("/catalog/initialize")
def initialize_catalog():
    """Endpoint to initialize the catalog
    
    Returns:
        dict: A message indicating success or failure
    """
    try:
        services.initialize_catalog()
        return {"message": "Catalog initialized successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/catalog/add_books")
def add_books_to_catalog():
    """Endpoint to add books to the catalog
    
    Returns:
        dict: A message indicating success or failure
    """
    try:
        services.add_books_to_catalog()
        return {"message": "Books added to catalog successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/catalog/books", response_model=List[BookDAO])
def get_all_books():
    """Endpoint to get all books from the catalog
    
    Returns:
        List[BookDAO]: A list of BookDAO objects representing all books in the catalog
    """
    try:
        return services.get_all_books()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/catalog/books/author/{author}", response_model=List[str])
def get_books_by_author(author: str):
    """Endpoint to get books by author
    
    Args:
        author (str): The author to search for
    
    Returns:
        List[str]: A list of book titles by the specified author
    """
    try:
        return services.get_books_by_author(author)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/catalog/books/isbn/{isbn}", response_model=List[str])
def get_books_by_isbn(isbn: str):
    """Endpoint to get books by ISBN
    
    Args:
        isbn (str): The ISBN to search for
    
    Returns:
        List[str]: A list of book titles with the specified ISBN
    """
    try:
        return services.get_books_by_isbn(isbn)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/catalog/books/title/{title}", response_model=List[str])
def get_books_by_title(title: str):
    """Endpoint to get books by title
    
    Args:
        title (str): The title to search for
    
    Returns:
        List[str]: A list of book titles with the specified title
    """
    try:
        return services.get_books_by_title(title)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))