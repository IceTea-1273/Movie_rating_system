from imdbDatabase import IMDbWrapper

class MovieSearch():

    def __init__(self, movie_title):
        self.movie_title = movie_title
        self.imdb_wrapper = IMDbWrapper()

    def search_movie(self):
        self.movies = self.imdb_wrapper.search_results(self.movie_title)
        if self.movies is None:  
            print("No movies found.")
            return False
        if len(self.movies) == 0:
            return False
        print("Search Results:")
        for idx, movie in enumerate(self.movies, start=1):
            title = movie.get('title', 'Unknown Title')
            year = movie.get('year', 'Unknown Year')
            print(f"{idx}. {title} ({year})")
        return True

    def choose_movie(self):
        if self.search_movie():
            while True:
                if self.movies is None:
                    return False
                if len(self.movies) == 0:
                    return False
                movie_id = input("Which movie from the list would you like to add? (nr) ")
                if not movie_id.isdigit():
                    print("Invalid choice. Please enter a valid number.")
                    continue
                movie_id = int(movie_id)
                if not (1 <= movie_id <= len(self.movies)):
                    print("Invalid choice. Please enter a valid number.")
                    continue
                selected_movie= self.imdb_wrapper.get_movie_details(movie_id)
                break
            return selected_movie


def movie_searcher():
    while True:
        movie_title = input("What movie are you looking for? ").strip()
        if not movie_title:
            print("Please enter a valid movie title.")
            continue
        searcher = MovieSearch(movie_title)
        selected_movie = searcher.choose_movie()
        if selected_movie == False:
            print("No movies found.")
            return False
        else:
            return selected_movie
    

    