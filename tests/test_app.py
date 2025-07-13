import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app

data = [
    {
        "id" : 1,
        "name" : "In Rainbows",
        "year" : 2007
    },
    {
        "id" : 2,
        "name" : "mikgazer vol.1",
        "year" : 2011
    }
]



@pytest.mark.asyncio
async def test_get_albums():
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url="http://test"
    ) as ac:
        response = await ac.get("/albums/")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json() == data

