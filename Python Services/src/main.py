from fastapi import FastAPI
from controllers import book_controller, catalog_controller, shoppingcart_controller
import uvicorn

app = FastAPI()

app.include_router(book_controller.router, prefix="/api")
app.include_router(catalog_controller.router, prefix="/api")
app.include_router(shoppingcart_controller.router, prefix="/api")

if __name__ == "__main__":   
    uvicorn.run(app, host="0.0.0.0", port=8080)