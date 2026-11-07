from fastapi import FastAPI

from app.api import books, categories
from app.db.db import engine, Base
from app.db import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Books API",
    description="REST API для управления каталогом книг и категорий",
    version="1.0.0"
)


app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "message": "API работает"
    }