# The purpose of guess game is to start a new game, cast a random number between 1 to
# variable called difficulty. The game will get a number input from the user
import random


class GuessGame:
    def __init__(self, difficulty: int):
        self._difficulty = int(difficulty)
        self._secret_number = self.generate_number()

    def generate_number(self):
        return random.randint(1, self._difficulty)

    def get_guess_from_user(self):
        player_guess = '0'
        while not player_guess.strip().isdigit() or int(player_guess) > self._difficulty or int(player_guess) < 1:
            player_guess = input(f"Please enter a number between 1 to {self._difficulty} and press ENTER \n")
            if not player_guess.strip().isdigit():
                print("Input can be Number (int) only! \n\n")
            elif int(player_guess) > self._difficulty or int(player_guess) < 1:
                print(f"Please choose a number between 1-{self._difficulty} only. \n\n")
        return int(player_guess)

    def compare_results(self, players_guess):
        # print(f"{type(secret_number)} ==? {type(players_guess)}")
        # print(secret_number == players_guess)
        return self._secret_number == players_guess

    def play(self):

        players_guess = self.get_guess_from_user()
        # print(f"Player choose {type(players_guess)}{players_guess}")
        return self.compare_results(players_guess)
