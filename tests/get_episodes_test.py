from anime_bot.infrastructure.sqlite_repository import SQLiteAnimeCatalogRepository

def test_get_episodes_by_anime_id(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)
    anime = repository.get_or_create_anime("Naruto")

    repository.save_episode(anime.id, 3, -100123, 503)
    repository.save_episode(anime.id, 1, -100123, 501)
    repository.save_episode(anime.id, 2, -100123, 502)

    episodes = repository.get_episodes_by_anime_id(anime.id)

    assert [episode.episode_number for episode in episodes] == [1, 2, 3]
    assert all(episode.anime_id == anime.id for episode in episodes)

def test_get_episode_by_id_returns_episode(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)
    anime = repository.get_or_create_anime("Naruto")

    saved_episode = repository.save_episode(
        anime_id=anime.id,
        episode_number=1,
        telegram_channel_id=-100123,
        telegram_message_id=501,
    )

    found_episode = repository.get_episode_by_id(saved_episode.id)

    assert found_episode == saved_episode

def test_get_episode_by_id_returns_none_when_episode_does_not_exist(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)

    episode = repository.get_episode_by_id(999)

    assert episode is None

def test_get_anime_by_id_returns_anime_with_genres(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)

    anime = repository.get_or_create_anime("Naruto")
    adventure = repository.get_or_create_genre("пригоди")
    comedy = repository.get_or_create_genre("комедія")

    repository.add_genre_to_anime(anime.id, adventure.id)
    repository.add_genre_to_anime(anime.id, comedy.id)

    found_anime = repository.get_anime_by_id(anime.id)

    assert found_anime is not None
    assert found_anime.id == anime.id
    assert found_anime.name == "Naruto"
    assert {genre.name for genre in found_anime.genres} == {"пригоди", "комедія"}

def test_get_anime_by_id_returns_none_when_anime_does_not_exist(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)

    assert repository.get_anime_by_id(999) is None