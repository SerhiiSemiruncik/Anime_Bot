import pytest
import os
import tempfile
from anime_bot.infrastructure.database import init_database

@pytest.fixture
def db_path() -> str:

    with tempfile.NamedTemporaryFile(suffix=".db", delete= False) as temp_db:
        path = temp_db.name

    init_database(path)

    yield path

    if os.path.exists(path):
        os.remove(path)