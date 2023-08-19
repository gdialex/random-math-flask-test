from flask import Flask, redirect
from random import randint, shuffle
from markupsafe import escape
from flask import url_for
import requests

SCORE = 0
app = Flask(__name__)


@app.route("/")
def index():
    global SCORE
    x = randint(2, 9)
    y = randint(2, 9)
    z = x * y
    L = [z, randint(10, 81), randint(10, 81), randint(10, 81)]
    shuffle(L)
    return (
        f"<h1>Your score is {SCORE}</h1>"
        f"<h2>{x}*{y}=?</h2>"
        f"<a href=/{'correct' if (L[0]==z) else 'wrong'}>{L[0]}</a><br>"
        f"<a href=/{'correct' if (L[1]==z) else 'wrong'}>{L[1]}</a><br>"
        f"<a href=/{'correct' if (L[2]==z) else 'wrong'}>{L[2]}</a><br>"
        f"<a href=/{'correct' if (L[3]==z) else 'wrong'}>{L[3]}</a><br>"
    )


@app.route("/correct")
def correct():
    global SCORE
    SCORE += 1
    return redirect(url_for("index"), code=302, Response=None)


@app.route("/wrong")
def wrong():
    global SCORE
    SCORE -= 1
    return redirect(url_for("index"), code=302, Response=None)
