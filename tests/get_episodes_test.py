from anime_bot.infrastructure.sqlite_repository import SQLiteAnimeCatalogRepository

def test_get_episodes_by_anime_id_returns_episodes_in_order(db_path):
    repository = SQLiteAnimeCatalogRepository(db_path)
    anime = repository.get_or_create_anime("Naruto")

    repository.save_episode(anime.id, 3, -100123, 503)
    repository.save_episode(anime.id, 1, -100123, 501)
    repository.save_episode(anime.id, 2, -100123, 502)

    episodes = repository.get_episodes_by_anime_id(anime.id)

    assert [episode.episode_number for episode in episodes] == [1, 2, 3]
    assert all(episode.anime_id == anime.id for episode in episodes)