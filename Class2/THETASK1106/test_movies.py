import movies


def test_create_movie(mock_movie):
    assert mock_movie.title == 'Interstellar'
    assert mock_movie.imdb_rating_0_to_10 == '8.7'
    assert mock_movie.release_year == '2014'


def test_add_movie_to_list(mock_movie):
    """
    Initiate MoviesIHaveSeenList and
    make it able to add items to it
    """
    my_seen_movies_list = movies.MoviesIHaveSeen()

    assert my_seen_movies_list.length == 0
    my_seen_movies_list.add_movie(mock_movie, '10')
    assert my_seen_movies_list.length == 1
    assert my_seen_movies_list.my_movies[0]['movie'] == 'Interstellar'


def test_remove_movie_from_list(mock_movie):
    my_seen_movies_list = movies.MoviesIHaveSeen()

    assert my_seen_movies_list.length == 0
    my_seen_movies_list.add_movie(mock_movie, '10')
    assert my_seen_movies_list.length == 1
    my_seen_movies_list.delete()
    assert my_seen_movies_list.length == 0


def test_movie_list_access(mock_movie):
    my_seen_movies_list = movies.MoviesIHaveSeen()
    my_seen_movies_list.add_movie(mock_movie, '10')
    my_seen_movies_list.add_movie(mock_movie, '10')
    assert my_seen_movies_list.my_movies == [{'movie': 'Interstellar', 'personal_rating_from_0_to_10': '10'},
                                             {'movie': 'Interstellar', 'personal_rating_from_0_to_10': '10'}]

def test_remove_specific_movie_from_list(mock_movie, mock_movie1, mock_movie2):
    my_seen_movies_list = movies.MoviesIHaveSeen()
    assert my_seen_movies_list.length == 0
    my_seen_movies_list.add_movie(mock_movie, '10')
    my_seen_movies_list.add_movie(mock_movie1, '10')
    my_seen_movies_list.add_movie(mock_movie2, '10')
    assert my_seen_movies_list.length == 3
    my_seen_movies_list.delete(1)
    assert my_seen_movies_list.my_movies[1]['movie'] == 'Spiderman'

