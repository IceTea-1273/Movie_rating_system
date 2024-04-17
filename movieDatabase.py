import imdb

moviesDB = imdb.IMDb()

movie_title = input('What movie are you looking for? ')
movies = moviesDB.search_movie(movie_title)
print(f'Searching for {movie_title}')
for movie in movies:
    title = movie['title']
    year = movie['year']
    print(f'{title}, {year}')

