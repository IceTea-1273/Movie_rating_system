import unittest
from unittest.mock import patch
from movieChoosing import MovieSearch

class TestMovieChoose_search(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class.")
        cls.movie_search = MovieSearch('Avengers')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_valid(self, mock_search_results):
        mock_search_results.return_value = [{'title': 'Avengers', 'year': '2012'}]
        result = self.movie_search.search_movie()
        self.assertTrue(result)
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
        mocked_print.assert_any_call('Search Results: ')
        mocked_print.assert_any_call('1. Avengers (2012)')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_no_movies_found(self, mock_search_results):
        mock_search_results.return_value = None
        result = self.movie_search.search_movie()
        self.assertFalse(result)
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
            mocked_print.assert_called_with('No movies found.')

    @patch('movieChoosing.IMDbWrapper.search_results')
    def test_search_movie_empty_results(self, mock_search_results):
        mock_search_results.return_value = []
        result = self.movie_search.search_movie()
        self.assertFalse(result)
        with patch('builtins.print') as mocked_print:
            self.movie_search.search_movie()
            mocked_print.assert_called_with('No movies found.')


if __name__ == '__main__':
    unittest.main()
