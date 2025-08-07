import unittest
import number_guesser
from unittest.mock import patch, call

class TestNumberGuesser(unittest.TestCase):

    def setUp(self):
        self.game = number_guesser.GuessingGame()
        self.game._test = True

    # Test Case - Win game on first guess (happy path)
    def test_play_prints_win_on_first_guess(self):
        with patch('builtins.print') as mock_print:
            self.game._winning_number = 2
            self.game._guess = 2
            self.game.play()
            mock_print.assert_has_calls([
                call(f'You have {self.game._guess_total} guesses remaining.'),
                call(f'Enter a number between {self.game._min_number} and {self.game._max_number}: '),
                call("That's the number!\n\nYou won!\n\ngame.play()\n")
                ])
            
    # Test Case - Win game on 2nd guess
        # Expected Result:

    # Test Case - Win game on 7th guess
        # Expected Result:

    # Test Case - Lose game (all 7 guesses incorrect)
            # Expected Result:
            
    # Test Case - Guess is valid number, but not winning number (too low) - first guess
        # Expected Result:

    # Test Case - Guess is valid number, but not winning number (too low) - last guess
            # Expected Result:

    # Test Case - Guess is valid number, but not winning number (too high) - first guess

    # Test Case - Guess is valid number, but not winning number (too high) - first guess
        # Expected Result:

    # Test Case - Guess is invalid, not an integer. I.e. Is a string "two" - first guess
            # Expected Result:

    # Test Case - Guess is invalid, not an integer. I.e. Is a string "two" - last guess
            # Expected Result:

    # Test Case - Guess is invalid. Is integer, but less than 1. I.e. 0 - first guess
            # Expected Result:

    # Test Case - Guess is invalid. Is integer, but less than 1. I.e. 0 - last guess
            # Expected Result:

    # Test Case - Guess is invalid. Is integer, but more than 99. I.e. 100 - first guess
            # Expected Result:

    # Test Case - Guess is invalid. Is integer, but more than 99. I.e. 100 - last guess
            # Expected Result:

if __name__ == '__main__':
    unittest.main()

# Example test cases
# def test_model(self):
#     self.assertEqual(self.car.model, 'Corolla')

# def test_set_model_raises(self):
#     with self.assertRaises(AttributeError):
#         self.car.model = 'Prius'

# @patch('builtins.print')
# def test_engine_start_prints(self, mock_print):
#     self.car.engine_start()
#     mock_print.assert_called_once_with('Car is running')