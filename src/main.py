from fastapi import FastAPI

from src.schemas import Album

app = FastAPI()

@app.get("/albums/", response_model=list[Album])
async def get_albums():
    return [
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


