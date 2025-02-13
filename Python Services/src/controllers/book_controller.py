from typing import List
from fastapi import APIRouter, HTTPException
from services.book_services import BookServices
from repositories.book import BookDAO

router = APIRouter()
services = BookServices()


@router.get("/books", response_model=List[BookDAO])
def get_all_books():
    """Endpoint to get all books
    
    Returns:
        List[BookDAO]: A list of BookDAO objects representing all books
    """
    try:
        return services.get_all_books()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))