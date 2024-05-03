import unittest
from unittest.mock import patch, MagicMock
from imdbDatabase import IMDbWrapper
from movieChoosing import MovieSearch

class TestMovieChoose_search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class.")
        cls.movie_search = MovieSearch('Avengers')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_valid(self, mock_search_results):
        print("1 Testing 'valid search'.")
        # Set up mock return value for search_results
        mock_search_results.return_value = [{'title': 'Avengers', 'year': '2012'}]
        # Call search_movie method
        result = self.movie_search.search_movie()

        # Assert that result is True (movie found)
        self.assertTrue(result)

        # Assert that print was called with the correct arguments
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
        mocked_print.assert_any_call('Search Results: ')
        mocked_print.assert_any_call('1. Avengers (2012)')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_no_movies_found(self, mock_search_results):
        print("1 Testing 'no movies found'.")
        mock_search_results.return_value = None
        result = self.movie_search.search_movie()
        self.assertFalse(result)
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
            mocked_print.assert_called_with('No movies found.')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_empty_results(self, mock_search_results):
        print("1 Testing 'empty results'.")
        mock_search_results.return_value = []
        result = self.movie_search.search_movie()
        self.assertFalse(result)
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
            mocked_print.assert_called_with('No movies found...')

class TestMovieSearch_choose(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.movie_search = MovieSearch('Avengers')

    def test_choose_movie_valid_input(self):
        print("2 Testing 'valid movie choice'")
        # Mock the search_movie method to return some movies
        with patch('movieChoosing.MovieSearch.search_movie') as mock_search_movie:
            # Mock that movies were found
            mock_search_movie.return_value = True
             # Mock the list of found movies
            mock_search_movie.movies = [{'title': 'Avengers', 'year': '2012'}]
            # Mock user input to select a valid movie
            with patch('builtins.input', return_value='1'):
                # Mock the get_movie_details method
                with patch('movieChoosing.IMDbWrapper.get_movie_details') as mock_get_movie_details:
                    # Mock the return value of get_movie_details
                    mock_get_movie_details.return_value = {'title': 'Avengers', 'year': '2012'}
                    # Call the choose_movie method
                    selected_movie = self.movie_search.choose_movie()
                    # Assert that selected_movie is not None
                    self.assertIsNotNone(selected_movie)
                    # Add additional assertions to verify the selected movie details if needed


                
    def test_choose_movie_invalid_input(self):
        # Mock the search_movie method to return some movies
        print("2 Testing 'invalid input'")
        with patch('movieChoosing.MovieSearch.search_movie') as mock_search_movie:
            mock_search_movie.return_value = True
            # Mock user input to provide an invalid choice
            with patch('builtins.input', side_effect=['abc', '0', '4']):
                selected_movie = self.movie_search.choose_movie()
                self.assertIsNone(selected_movie)
                # Add assertions to verify how invalid input is handled
                
    def test_choose_movie_no_movies_found(self):
        # Mock the search_movie method to return no movies
        print("2 Testing 'no movies found'")
        with patch('movieChoosing.MovieSearch.search_movie') as mock_search_movie:
            mock_search_movie.return_value = False
            movie_search = MovieSearch('Nonexistent Movie')
            selected_movie = movie_search.choose_movie()
            self.assertIsNone(selected_movie)
            # Add assertions to verify how the method handles no movies found




if __name__ == '__main__':
    unittest.main()
