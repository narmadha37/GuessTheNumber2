# test_guess_game.py

import unittest
from guess_game import generate_random_number

class TestGuessGame(unittest.TestCase):

    def test_generate_random_number(self):
        number = generate_random_number()
        self.assertTrue(1000 <= number <= 9999, "Random number should have four digits")

if __name__ == '__main__':
    unittest.main()
