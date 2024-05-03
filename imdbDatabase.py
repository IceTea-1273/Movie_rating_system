import imdb

class IMDbWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.__moviesDB = imdb.IMDb()

    def search_results(self, movie_title):
        try:
            print(f'Searching for "{movie_title}"...')
            self.movies = self.__moviesDB.search_movie(movie_title)
            return self.movies
        except imdb.IMDbError as e:
            print(f"An error occurred: {e}")
            return None

    def get_movie_details(self, movie_id):
        try:
            id = self.movies[movie_id-1].getID()
            movie = self.__moviesDB.get_movie(id)
            return movie['title']
        except imdb.IMDbError as e:
            print(f"An error occurred: {e}")
            return None