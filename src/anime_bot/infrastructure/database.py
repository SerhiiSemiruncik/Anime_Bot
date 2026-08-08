import sqlite3

def init_database(database_path: str) -> None:

    try:
        with sqlite3.connect(database_path) as database:
            cursor = database.cursor()

            cursor.execute("PRAGMA foreign_keys = ON;")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anime 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(255) UNIQUE NOT NULL
                ) 
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(50) UNIQUE NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS anime_genres 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 anime_id INTEGER NOT NULL,
                 genre_id INTEGER NOT NULL,
                 FOREIGN KEY (anime_id) REFERENCES anime(id), 
                 FOREIGN KEY (genre_id) REFERENCES genres(id),
                 UNIQUE (anime_id, genre_id)
                 )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS episodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                anime_id INTEGER NOT NULL,  
                episode_number INTEGER NOT NULL,
                telegram_channel_id INTEGER NOT NULL,
                telegram_message_id INTEGER NOT NULL,
                FOREIGN KEY (anime_id) REFERENCES anime(id),
                UNIQUE (anime_id, episode_number)
                )
            """)

            database.commit()

    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return