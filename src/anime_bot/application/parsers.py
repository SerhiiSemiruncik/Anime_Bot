from dataclasses import dataclass

@dataclass(frozen=True)
class ParsedAnimePost:
    anime_name: str
    episode_number: int
    genres: tuple[str, ...]

class ChannelPostParser:
    def parse(self, text: str) -> ParsedAnimePost | None:
        """
        Parses channel post text and returns ParsedAnimePost.
        Returns None if the post format is invalid.
        """
        if not text.strip():
            return None

        lines = text.splitlines()

        anime_name = None
        episode_number = None
        genres = []

        for line in lines:
            line = line.strip()
            if line.startswith("Назва:"):
                anime_name = line[len("Назва:"):].strip()
            if line.startswith("Серія:"):
                try:
                    episode_number = int(line[len("Серія:"):].strip())
                except ValueError:
                    return None
            if line.startswith("#"):
                for word in line.split():
                    if word.startswith("#"):
                        genre = word.lstrip("#").strip()

                        if genre:
                            genres.append(genre)

        if not anime_name or episode_number is None:
            return None
        return ParsedAnimePost(anime_name, episode_number, tuple(genres))

