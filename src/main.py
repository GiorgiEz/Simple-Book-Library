from fastapi import FastAPI, Query, HTTPException
from models import Book
from typing import Annotated
from database import create_db_and_tables, SessionDep
from sqlmodel import select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Creates a book
@app.post("/books/")
def create_book(book: Book, session: SessionDep) -> Book:
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

# Lists all the books
@app.get("/books/")
def read_books(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Book]:
    books = session.exec(select(Book).offset(offset).limit(limit)).all()
    return books

# Reads one book by id
@app.get("/books/{book_id}")
def read_book(book_id: int, session: SessionDep) -> Book:
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Deletes a book by id
@app.delete("/books/{book_id}")
def delete_book(book_id: int, session: SessionDep):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    session.delete(book)
    session.commit()
    return {"ok": True}
