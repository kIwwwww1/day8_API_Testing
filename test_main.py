import pytest
from httpx import AsyncClient, ASGITransport
from .main import app, books

@pytest.mark.asyncio
async def test_get_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        resp = await ac.get('/books')
        assert resp.status_code == 200
        assert len(books) == 2



@pytest.mark.asyncio
async def test_post_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        resp = await ac.post('/books', json={
        "id": 3, 
        "title": "Test",
        "description": "kIww1",
        "year": "2025",

        })
        assert resp.status_code == 200
        data = resp.json() 
        assert data['id'] == 3
        assert len(books) == 3