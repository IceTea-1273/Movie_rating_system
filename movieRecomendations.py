import openaiAPI as ai
import re
import os

class RecomendMovies:

    def random_movies(self):
        movie_input = "Give me random 5 movies to watch amd their release year"
        response = ai.chat_with_gpt(movie_input)
        print("Random movie recomendation: \n", response)

    def similar_movie(self):
        user_input = input("Please enter the title of a movie you enjoyed, and we'll provide you with a recommendation for a similar movie: ")
        movie_input = (f"Give me a movie recomendation similar to {user_input}.\n")
        response = ai.chat_with_gpt(movie_input)
        print("\n", response)

    def movie_genre(self):
        user_input = input("Please enter a genre of a movie you would like to see: ")
        movie_input = (f"Give me a {user_input} movie recomendation.\n")
        response = ai.chat_with_gpt(movie_input)
        print("\n", response)

    def from_watched(self, username):
        user_dir = os.path.join(os.curdir, "userProfiles", username, "WATCHED.txt")
        with open(user_dir, 'r') as f:
            existing_movies = []
            for line in f:
                match = re.search(r"'(.*?)'", line)
                if match:
                    existing_movies.append(match.group(1))
        user_input = " ".join(existing_movies)
        movie_input = (f"Give me 3 movie recomendations based on these movies: {user_input}\n")
        print("\nRecomended movies, based on your watched list" )
        response = ai.chat_with_gpt(movie_input)
        print(response)    