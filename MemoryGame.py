from time import sleep
import random
import functools
import os

class MemoryGame:
    def __init__(self, difficulty: int):
        self._difficulty = difficulty

    def generate_sequence(self):
        sequence = []
        for i in range(0, self._difficulty):
            sequence.append(random.randint(1, 101))
        return sequence

    def get_list_from_user(self):
        player_sequence = []
        for i in range(0, self._difficulty):
            player_guess = '0'
            while not player_guess.strip().isdigit() or int(player_guess) > 101 or int(player_guess) < 1:
                player_guess = input(f"Please enter your {i+1} number, (should be between 1 to 101) and press ENTER \n")
                if not player_guess.strip().isdigit():
                    print("Input can be Number (int) only! \n\n")
                elif int(player_guess) > 101 or int(player_guess) < 1:
                    print(f"Please choose a number between 1-101 only. \n\n")
            player_sequence.append(int(player_guess))
        return player_sequence

    def is_list_equal(self, listA: [], listB: []):
        return functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, listA, listB))

    def play(self):
        computer_sequence = self.generate_sequence()
        print(f"Try to momorize and repeat the following sequence: \n {computer_sequence}")
        sleep(0.7)
        for i in range(1,100):
            print(f"\n")
        player_sequence = self.get_list_from_user()
        return self.is_list_equal(computer_sequence, player_sequence)
