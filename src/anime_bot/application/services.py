from anime_bot.application.parsers import ChannelPostParser
from anime_bot.domain.repositories import AnimeCatalogRepository

class ChannelPostService:

    def __init__(self, parser: ChannelPostParser, repository: AnimeCatalogRepository):
        self.parser = parser
        self.repository = repository

    def process_channel_post(self, text: str, telegram_channel_id: int, telegram_message_id: int) -> None:

        parsed_post = self.parser.parse(text)

        if parsed_post is None:
            return

        anime = self.repository.get_or_create_anime(parsed_post.anime_name)
        for genre_name in parsed_post.genres:
            genre = self.repository.get_or_create_genre(genre_name)
            self.repository.add_genre_to_anime(anime.id, genre.id)

        self.repository.save_episode(
            anime_id=anime.id,
            episode_number=parsed_post.episode_number,
            telegram_channel_id=telegram_channel_id,
            telegram_message_id=telegram_message_id,
        )