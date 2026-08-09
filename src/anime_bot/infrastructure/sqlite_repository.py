import sqlite3

from anime_bot.domain.entities import Anime, Genre

class SQLiteAnimeCatalogRepository:
    def __init__(self, database_path: str) -> None:
        self.database_path = database_path

    def get_or_create_anime(self, name: str) -> Anime:

        name = name.strip()
        if not name:
            raise ValueError("Anime name cannot be empty")

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            try:
                cursor.execute("SELECT id, name FROM anime WHERE name = ?", (name,))
                row = cursor.fetchone()
                if row:
                    anime_id, anime_name = row
                    return Anime(id=anime_id, name=anime_name, genres=())
                else:
                    cursor.execute("INSERT INTO anime (name) VALUES (?)", (name,))
                    anime_id = cursor.lastrowid
                    conn.commit()
                    return Anime(id=anime_id, name=name, genres=())
            except sqlite3.Error:
                raise

    def get_or_create_genre(self, name: str) -> Genre:

        name = name.strip()
        if not name:
            raise ValueError("Genre name cannot be empty")

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            try:
                cursor.execute("SELECT id, name FROM genres WHERE name = ?", (name,))
                row = cursor.fetchone()
                if row:
                    genre_id, genre_name = row
                    return Genre(id=genre_id, name=genre_name)
                else:
                    cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
                    genre_id = cursor.lastrowid
                    conn.commit()
                    return Genre(id=genre_id, name=name)
            except sqlite3.Error:
                raise

    def add_genre_to_anime(self, anime_id: int, genre_id: int) -> None:

        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            try:
                cursor.execute(
                    "INSERT OR IGNORE INTO anime_genres (anime_id, genre_id) VALUES (?, ?)",
                    (anime_id, genre_id),
                )
                conn.commit()
            except sqlite3.Error:
                raise
