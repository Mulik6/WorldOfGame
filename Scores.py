# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he own will be added to his current amount of
# point saved in a file.

import Utils
from os.path import exists


# The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.
def add_score(difficulty: int):
    file_exists = exists(Utils.SCORES_FILE_NAME)
    # current_score = 0
    if not file_exists:
        open(Utils.SCORES_FILE_NAME, "a")
    with open(Utils.SCORES_FILE_NAME, "r") as scores_file:
        current_score = scores_file.read()
        print(f"current score: {current_score}")
    if current_score == '':
        current_score = 0
    new_score = int(current_score) + (difficulty * 3) + 5
    print(f"new_score:{new_score}")
    with open(Utils.SCORES_FILE_NAME, "w") as scores_file:
        scores_file.write(f"{new_score}")


