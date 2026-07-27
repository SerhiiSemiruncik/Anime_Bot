from anime_bot.application.parsers import ChannelPostParser
from anime_bot.application.services import ChannelPostService
from anime_bot.domain.entities import Anime, Episode, Genre


class FakeAnimeCatalogRepository:
    def __init__(self):
        self.anime_names = []
        self.genre_names = []
        self.anime_genre_links = []
        self.episodes = []

    def get_or_create_anime(self, name: str) -> Anime:
        self.anime_names.append(name)
        return Anime(id=1, name=name, genres=())

    def get_or_create_genre(self, name: str) -> Genre:
        self.genre_names.append(name)
        genre_id = len(self.genre_names)
        return Genre(id=genre_id, name=name)

    def add_genre_to_anime(self, anime_id: int, genre_id: int) -> None:
        self.anime_genre_links.append((anime_id, genre_id))

    def save_episode(
        self,
        anime_id: int,
        episode_number: int,
        telegram_channel_id: int,
        telegram_message_id: int,
    ) -> Episode:
        episode = Episode(
            id=1,
            anime_id=anime_id,
            episode_number=episode_number,
            telegram_channel_id=telegram_channel_id,
            telegram_message_id=telegram_message_id,
        )

        self.episodes.append(episode)
        return episode


def test_process_channel_post_saves_anime_genres_links_and_episode():
    parser = ChannelPostParser()
    repository = FakeAnimeCatalogRepository()
    service = ChannelPostService(parser=parser, repository=repository)

    text = """Назва: Наруто
Серія: 1
#пригоди #комедія"""

    service.process_channel_post(
        text=text,
        telegram_channel_id=-100123,
        telegram_message_id=555,
    )

    assert repository.anime_names == ["Наруто"]
    assert repository.genre_names == ["пригоди", "комедія"]
    assert repository.anime_genre_links == [(1, 1), (1, 2)]

    assert repository.episodes == [
        Episode(
            id=1,
            anime_id=1,
            episode_number=1,
            telegram_channel_id=-100123,
            telegram_message_id=555,
        )
    ]