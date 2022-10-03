import requests
import random


class CurrencyRouletteGame:
    def __init__(self, difficulty: int):
        self._difficulty = difficulty
        # Currency API:
        API_KEY = 'f3ba3a31fd164f767910795c'
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
        response = requests.get(url, verify=False)
        data = response.json()
        self.usd_to_nis = int(data['conversion_rates']['ILS'])
        self.random_amount = random.randint(1, 100)

    def get_money_interval(self):
        lower_threshold = self.random_amount * (self.usd_to_nis - (5 - self._difficulty))
        higher_threshold = self.random_amount * (self.usd_to_nis + (5 - self._difficulty))
        return (lower_threshold, higher_threshold)

    def get_guess_from_user(self):
        player_guess = 'a'
        while not player_guess.strip().isdigit():
            player_guess = input(f"Try and guess the amount of {self.random_amount} in ILS: \n")
            if not player_guess.strip().isdigit():
                print("Input can be Number (int) only! \n\n")
        return int(player_guess)

    def play(self):
        print(f"Hello and welcome to CurrencyRouletteGame!")
        interval = self.get_money_interval()
        player_guess = self.get_guess_from_user()
        return interval[0] < player_guess < interval[1]

