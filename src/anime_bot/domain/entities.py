from dataclasses import dataclass

@dataclass(frozen=True)
class Genre:
    id: int
    name: str

@dataclass(frozen=True)
class Anime:
    id: int
    name: str
    genres: tuple[Genre, ...]

@dataclass(frozen=True)
class Episode:
    id: int
    anime_id: int
    episode_number: int
    telegram_channel_id: int
    telegram_message_id: int
