import os
import sqlite3
import tempfile

import pytest

from anime_bot.infrastructure.database import init_database
from anime_bot.infrastructure.sqlite_repository import SQLiteAnimeCatalogRepository

@pytest.fixture
def db_path() -> str:

    with tempfile.NamedTemporaryFile(suffix=".db", delete= False) as temp_db:
        path = temp_db.name

    init_database(path)

    yield path

    if os.path.exists(path):
        os.remove(path)

def test_anime_genres_uniqueness(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)

    anime = repository.get_or_create_anime("Naryto")
    genre = repository.get_or_create_genre("Horror")

    repository.add_genre_to_anime(anime.id, genre.id)

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT COUNT(*) 
            FROM anime_genres 
            WHERE anime_id = ? AND genre_id = ?
            """,
            (anime.id, genre.id)
        )
        assert cursor.fetchone()[0] == 1

    repository.add_genre_to_anime(anime.id, genre.id)

    #Check to make sure there is still only one entry, not two
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM anime_genres")
        assert cursor.fetchone()[0] == 1