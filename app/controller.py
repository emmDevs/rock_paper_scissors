from flask import render_template, request, redirect, url_for
from app import app
from app.models.game import *
from app.models.player import *
from app.models.games import players, play_game

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/play-game', methods=['POST'])
# def play_game():
#     player1


@app.route('/computer-vs-computer', methods=['GET'])
def computer_vs_computer():
    player1 = Player("Bob", "scissors")
    player2 = Player("Alice", "rock")
    players = (player1, player2)
    play_game(player1, player2)
    winner = play_game(player1, player2)
    return render_template('computer-vs-computer.html', title="Computer Vs Computer", players=players, winner=play_game, player1=player1, player2=player2)


# @app.route('/play-game', <player1>, <player2)
# def play_game(player1, player2):
#     player1 = Player("Bob", "scissors")
#     player2 = Player("Alice", "rock")
#     winner = play_game()
#     # game=Game(player1, player2)
#     # # result = game.play_game()
#     return redirect('/computer-vs-computer', players=players, play_game=play_game(player1, player2))
 
