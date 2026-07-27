from anime_bot.application.parsers import ChannelPostParser, ParsedAnimePost

def test_parse_valid_post():
    parser = ChannelPostParser()
    text = """
    Назва: My Hero Academia
    Серія: 5
    #Action #Adventure #Superhero
    """
    result = parser.parse(text)
    assert result == ParsedAnimePost(
        anime_name="My Hero Academia",
        episode_number=5,
        genres=("Action", "Adventure", "Superhero")
    )

def test_parse_invalid_post():
    parser = ChannelPostParser()

    result = parser.parse(" ")

    assert result is None

def test_parse_post_without_anime_name_returns_none():

    parser = ChannelPostParser()
    text = """
    Серія: 5
    #Action #Adventure #Superhero
    """
    result = parser.parse(text)
    assert result is None

def test_parse_post_with_invalid_episode_returns_none():
    parser = ChannelPostParser()
    text = """
    Назва: My Hero Academia
    Серія: five
    #Action #Adventure #Superhero
    """
    result = parser.parse(text)
    assert result is None