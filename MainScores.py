# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with
# HTML. This will be done by using python’s flask library.
from flask import Flask
import Utils


def score_server():
    app = Flask(__name__)

    @app.route("/")
    def return_scores():
        try:
            with open(Utils.SCORES_FILE_NAME,"r") as score_file:
                SCORE = score_file.readlines()[-1:]
                print(SCORE)
            return f"""<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <h1>The score is <div id="score">{SCORE}</div></h1>
                    </body>
                    </html>"""
        except Exception as ERROR:
            return f"""<html>
                    <head>
                    <title>Scores Game</title>
                    </head>
                    <body>
                    <body>
                    <h1><div id="score" style="color:red">{ERROR}</div></h1>
                    </body>
                    </html>"""

    app.run("0.0.0.0", 5000)
