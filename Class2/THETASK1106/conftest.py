import pytest
import movies

@pytest.fixture()
def mock_movie():
    result = movies.Movie('Interstellar', '8.7', '2014')
    return result


@pytest.fixture()
def mock_movie1():
    result = movies.Movie('Spiderman', '2.1', '2059')
    return result


@pytest.fixture()
def mock_movie2():
    result = movies.Movie('Avatar', '3', '2005')
    return result