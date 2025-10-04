from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Simple Books CRUD API")

class Book(BaseModel):
    id: int
    title: str = Field(..., min_length=1, max_length=100)
    description: str
    year: str

books = [
    {
        "id": 1,
        "title": "Harry Potter",
        "description": "J. K. Rowling",
        "year": "2001",
    },
    {
        "id": 2,
        "title": "Dune",
        "description": "Frank Herbert",
        "year": "1965",
    },
]

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def create_book(book: Book):
    for b in books:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book.model_dump())
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            books[index] = updated_book.dict()
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, b in enumerate(books):
        if b["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
