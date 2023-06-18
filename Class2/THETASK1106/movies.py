class Movie:
    def __init__(self, title, imdb_rating_0_to_10, release_year):
        self.title = title
        self.imdb_rating_0_to_10 = imdb_rating_0_to_10
        self.release_year = release_year

    def __repr__(self):
        return repr({"title": self.title, "imdb_rating_0_to_10": self.imdb_rating, "release_year": self.release_year})


class MoviesIHaveSeen:
    def __init__(self):
        self.my_movies = []
        self.length = 0

    def __len__(self):
        return len(self.my_movies)

    def add_movie(self, movie, personal_rating_from_0_to_10):
        self.my_movies.append({'movie': movie.title, 'personal_rating_from_0_to_10': personal_rating_from_0_to_10})
        self.length = len(self.my_movies)

    def delete(self, id=-1):
        if id == -1:
            self.my_movies.pop()
        elif id in range(0, 999):
            self.my_movies.pop(id)
        self.length = len(self.my_movies)

#available_items = []
# movies_list = MoviesIHaveSeen()
# while True:
#     action = input("This is your movies list program, What you want to do? a - add new movie, b - show movies i have seen list, "
#                    "d - delete last movie, q - exit")
#     if action == 'a':
#         movie_title = input("Enter the movie's name: ")
#         movie_imdb_rating_0_to_10_ = input("Enter the movie's IMDB rating: ")
#         movie_release_year = input("Enter the movie's release year: ")
#
#         item = Item(item_name, item_origin)
#         available_items.append(item)
#         shopping_list.add_item(item, item_amount)
#     elif action == 'b':
#         print(shopping_list.items)
#     elif action == 'c':
#         print(available_items)
#     elif action == 'd':
#         shopping_list.delete()
#     elif action == 'q':
#         break
