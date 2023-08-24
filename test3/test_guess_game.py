import unittest
from unittest.mock import patch
from guess_game import generate_random_number, check_guess, game_loop

class TestGuessGame(unittest.TestCase):

    def test_generate_random_number(self):
        number = generate_random_number()
        self.assertTrue(1000 <= number <= 9999, "Random number should have four digits")

    def test_check_guess(self):
        secret_number = "1234"
        self.assertEqual(check_guess(secret_number, "1234"), ["circle","circle","circle","circle"])
        self.assertEqual(check_guess(secret_number, "1243"), ["circle","circle","X","X"])
        self.assertEqual(check_guess(secret_number, "4321"), ["X","X","X","X"])
        self.assertEqual(check_guess(secret_number, "5678"), [])

    @patch('builtins.input', side_effect=['1234', 'q'])
    @patch('builtins.print')
    def test_game_loop_win(self, mock_print, mock_input):
        # Set the secret number to '1234'
        secret_number = '1234'

        # Generate a new random number for the test
        with patch('random.randint', return_value=int(secret_number)):
            game_loop()

        mock_print.assert_any_call("Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        mock_print.assert_any_call("Thanks for playing!")

if __name__ == '__main__':
    unittest.main()

