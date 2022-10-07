from os import system

SCORES_FILE_NAME = 'Scores.txt'  # A string representing a file name. By default “Scores.txt”
BAD_RETURN_CODE = '418'  # A number representing a bad return code for a function.


# function to clear the screen (useful when playing memory game or
# before a new game starts).
def screen_cleaner():
    system('cls')
