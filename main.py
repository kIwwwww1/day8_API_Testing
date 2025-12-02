from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

books = [
    {'id': 1,
     'title': 'Гогаль',
     'author': 'Мертвые души',
     },

     {'id': 2,
     'title': 'Тургенев',
     'author': 'Муму',
     }
]

class NewBook(BaseModel):
    title: str 
    author: str


class Book(NewBook):
    id: int = Field(default=len(books) + 1)


@app.post('/add_book')
async def add_book(new_book: Book):
    book = {
        'id': new_book.id,
        'title': new_book.title,
        'author': new_book.author,
        }
    books.append(book)
    return {'True': 'message: Книга добавлена'}


@app.get('/books')
async def get_all_books() -> list[dict]:
    return books

