import imdb

class IMDbWrapper:
    def __init__(self):
        self.moviesDB = imdb.IMDb()

    def search_results(self, movie_title):
        try:
            print(f'Searching for "{movie_title}"...')
            self.movies = self.moviesDB.search_movie(movie_title)
            return self.movies
        except imdb.IMDbError as e:
            print(f"An error occurred: {e}")
            return None

    def get_movie_details(self, movie_id):
        try:
            id = self.movies[movie_id-1].getID()
            movie = self.moviesDB.get_movie(id)
            return movie['title']
        except imdb.IMDbError as e:
            print(f"An error occurred: {e}")
            return None
