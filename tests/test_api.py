import pytest
from httpx import AsyncClient, ASGITransport
from main import app, Book

@pytest.mark.asyncio
async def test_get_all_books():
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url='http://test'
    ) as ac:
        respons = await ac.get('/books')
        assert respons.status_code == 200
        data = respons.json()
        assert len(data) == 2
        for book in data:
            assert Book(**book)

@pytest.mark.asyncio
async def test_add_book():
    async with AsyncClient(
        transport=ASGITransport(app=app), 
        base_url='http://test'
    ) as ac:
        respons = await ac.post('/add_book', json={
            'title': 'Test title',
            'author': 'Test author'
        })
        assert respons.status_code == 200
        data = respons.json()
        assert data == {'True': 'message: Книга добавлена'}