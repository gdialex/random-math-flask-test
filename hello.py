from flask import Flask
from random import randint, shuffle
from markupsafe import escape
from flask import url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    x = randint(2,9)
    y = randint(2,9)
    z = x*y
    L = [z, randint(10, 81), randint(10, 81), randint(10, 81)]
    shuffle(L)
    score = 0
    return (
                f'<p>{x}*{y}=?</p>'
                f'<a href=/{score + 1 * (L[0]==z)}>{L[0]}</a><br>'
                f'<a href=/{score + 1 * (L[1]==z)}>{L[1]}</a><br>'
                f'<a href=/{score + 1 * (L[2]==z)}>{L[2]}</a><br>'
                f'<a href=/{score + 1 * (L[3]==z)}>{L[3]}</a><br>'
    )

@app.route('/<int:score>')
def index_continue(score):
    x = randint(2,9)
    y = randint(2,9)
    z = x*y
    L = [z,randint(10,81),randint(10,81),randint(10,81)]
    shuffle(L)
    return (
                f'<h1>You have {score} points!</h1>'
                f'<p>{x}*{y}=?</p>'
                f'<a href=/{score + 1 * (L[0]==z)}>{L[0]}</a><br>'
                f'<a href=/{score + 1 * (L[1]==z)}>{L[1]}</a><br>'
                f'<a href=/{score + 1 * (L[2]==z)}>{L[2]}</a><br>'
                f'<a href=/{score + 1 * (L[3]==z)}>{L[3]}</a><br>'
    )