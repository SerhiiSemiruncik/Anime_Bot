from anime_bot.domain.entities import Genre, Anime, Episode


class AnimeCatalogRepository:

    def get_or_create_anime(self, name: str) -> Anime:
        pass

    def get_or_create_genre(self, name: str) -> Genre:
        pass

    def save_episode(
        self,
        anime_id: int,
        episode_number: int,
        telegram_channel_id: int,
        telegram_message_id: int,
    ) -> Episode:
        pass

    def get_anime_by_id(self, anime_id: int) -> Anime | None:
        pass

    def search_anime_by_name(self, name: str) -> list[Anime]:
        pass

    def search_anime_by_genre(self, genre_name: str) -> list[Anime]:
        pass

    def get_all_anime(self) -> list[Anime]:
        pass

    def get_episodes_by_anime_id(self, anime_id: int) -> list[Episode]:
        pass

    def get_episode_by_id(self, episode_id: int) -> Episode | None:
        pass

    def get_all_genres(self) -> list[Genre]:
        pass

    def add_genre_to_anime(self, anime_id: int, genre_id: int) -> None:
        pass