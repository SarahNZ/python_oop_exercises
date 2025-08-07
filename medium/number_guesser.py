# Assume the number is inclusive of 1 and less than 100

import random

class GuessingGame():

    def __init__(self):
        self._min_number = 1
        self._max_number = 100
        self._guess_total = 7
        self._winning_number = 2
        # self._winning_number =  random.randint(self._min_number, self._max_number) # includes 1 but not 100
        self._guess_count = 0
        self._guess = None
        self._guesses_remaining = self._guess_total
        self._test = False 

    def play(self):
        print(f"You have {self._guesses_remaining}"
              " guesses remaining.")
        
        self._input_guess()

        # if self._guess_is_valid():
        if self._guess == self._winning_number:
            print("That's the number!\n\nYou won!\n\ngame.play()\n")
            # self._new_game()
        else:
            print('Your guess is wrong')
            # print(f"Your guess is too {self._high_or_low(self._guess)}.\n\n")
            # self.play()

    # def _high_or_low(self):
    #     if self._guess < self._winning_number:
    #         return "low"
    #     else:
    #         return "high"

    def _input_guess(self):
        print(f'Enter a number between {self._min_number} and {self._max_number}: ')
        try:
            if self._test == False:
                self._guess = input()
                self._guess = int(self._guess)
        except (NameError, TypeError, ValueError):
            print(f"Invalid guess.")
            # self._input_guess()

    # def _guess_is_valid(self):
    #         if 1 <= self._guess < 100:
    #         else:
    #             print(f"Invalid guess. {self._input_guess()}")

    def _is_winning_number(self):
        return 
    
    # def _new_game(self):
    #     # self._winning_number =  random.randint(self._min_number, self._max_number) # includes 1 but not 100
    #     self._winning_number = 2
    #     self._guess_count = 0
    #     self._guess = None
    #     self._guesses_remaining = self._guess_total

# game = GuessingGame()
# game.play()