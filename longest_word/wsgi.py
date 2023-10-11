# pylint: disable=missing-docstring


from flask import Flask, render_template, request, session
from longest_word.game import Game
from flask_session import Session

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = '/tmp'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    game = Game()
    session['score']=session.get('score',0)
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    if is_valid:
        session['score']+=len(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word, score=session['score'])
