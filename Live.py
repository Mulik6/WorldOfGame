import CurrencyRouletteGame
import GuessGame
import MemoryGame


def welcome(name="Muli"):
    return (f"Hello {name} and welcome to the World of Games (WoG). \n"
            f"Here you can find many cool games to play.")


def load_game():
    player_choose = "0"
    game_difficulty = "0"
    while not player_choose.strip().isdigit() or int(player_choose) > 3 or int(player_choose) < 1:
        player_choose = input("Please choose a game to play: \n"
                              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess "
                              "it back \n "
                              "2. Guess Game - guess a number and see if you chose like the computer \n"
                              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n")
        if not player_choose.strip().isdigit():
            print("Input can be Number (int) only! \n\n")
        elif int(player_choose) > 3 or int(player_choose) < 1:
            print("Please choose a number between 1-3 only. \n\n")

    while not game_difficulty.strip().isdigit() or int(game_difficulty) > 5 or int(game_difficulty) < 1:
        game_difficulty = input("Please choose game difficulty from 1 to 5: ")
        if not game_difficulty.strip().isdigit():
            print("Input can be Number (int) only! \n\n")
        elif int(game_difficulty) > 5 or int(game_difficulty) < 1:
            print("Please choose a number between 1-5 only. \n\n")

    # Initiate and start game

    if player_choose == "1":
        print(GuessGame.GuessGame(int(game_difficulty)).play())
    elif player_choose == "2":
        print(MemoryGame.MemoryGame(int(game_difficulty)).play())
    elif player_choose == "3":
        print(CurrencyRouletteGame.CurrencyRouletteGame(int(game_difficulty)).play())
