from fastapi import FastAPI
from .database import create_db_and_tables
from .routes import books

app = FastAPI()

@app.on_event("startup")
def on_startup():
    """
    Event handler to create database and tables on application startup.
    """
    create_db_and_tables()

@app.get("/")
def home():
    return {
        "message": "Welcome to the Book Library API!",
        "docs_url": "http://127.0.0.1:8000/docs"
    }

app.include_router(books.router)
