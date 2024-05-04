import unittest
from unittest.mock import patch
import profileManaging

class TestValidation(unittest.TestCase):

    def setUp(self):
        self.validator = profileManaging.Validation()

    def test_valid_email(self):
        valid_email = "text@example.com"
        self.assertTrue(self.validator._is_valid_email(valid_email))

    def test_invalid_email(self):
        invalid_email = "invalid@email"
        self.assertFalse(self.validator._is_valid_email(invalid_email))

    
    @patch('profileManaging.pwinput.pwinput')
    @patch('builtins.print')
    def test_get_valid_password_too_short(self, mock_print, mock_pwinput):
        mock_pwinput.side_effect = ['pass', '12345678']
        password = self.validator._get_valid_password()
        self.assertEqual(password, '12345678')
        mock_print.assert_called_with("Password must be 8-20 characters long.")

    @patch('profileManaging.pwinput.pwinput')
    @patch('builtins.print')
    def test_get_valid_password_valid_length(self, mock_print, mock_pwinput):
        mock_pwinput.side_effect = ['123456789']
        password = self.validator._get_valid_password()
        self.assertEqual(password, '123456789')
        mock_print.assert_not_called()  # No error message should be printed

    @patch('profileManaging.pwinput.pwinput')
    @patch('builtins.print')
    def test_get_valid_password_too_long(self, mock_print, mock_pwinput):
        mock_pwinput.side_effect = ['password12345678901234567890', '12345678']
        password = self.validator._get_valid_password()
        self.assertEqual(password, '12345678')
        mock_print.assert_called_with("Password must be 8-20 characters long.")

    def test_valid_username(self):
        valid_username1 = "valid_username"
        valid_username2 = "user-name"
        valid_username3 = "Val1d.(usern4me)"
        self.assertTrue(self.validator._is_valid_username(valid_username1))
        self.assertTrue(self.validator._is_valid_username(valid_username2))
        self.assertTrue(self.validator._is_valid_username(valid_username3))

    def test_invalid_username(self):
        invalid_username1 = "invalid username"
        invalid_username2 = " "
        invalid_username3 ="1"
        self.assertFalse(self.validator._is_valid_username(invalid_username1))
        self.assertFalse(self.validator._is_valid_username(invalid_username2))
        self.assertFalse(self.validator._is_valid_username(invalid_username3))

    def test_valid_date(self):
        valid_date1 = "2000 01 01"
        valid_date2 = "2024 05 04"
        self.assertTrue(self.validator._is_valid_date_of_birth(valid_date1))
        self.assertTrue(self.validator._is_valid_date_of_birth(valid_date2))
      
    
    def test_invalid_date(self):
        invalid_date1 = "2000 01"
        invalid_date2 = "2024 05 04 01"
        invalid_date3 = ""
        invalid_date4 = "2011 13 13"
        invalid_date5 = "2011 12 32"

        self.assertFalse(self.validator._is_valid_date_of_birth(invalid_date1))
        self.assertFalse(self.validator._is_valid_date_of_birth(invalid_date2))
        self.assertFalse(self.validator._is_valid_date_of_birth(invalid_date3))
        self.assertFalse(self.validator._is_valid_date_of_birth(invalid_date4))
        self.assertFalse(self.validator._is_valid_date_of_birth(invalid_date5))

if __name__ == "__main__":
    unittest.main()