from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *
from app.models.games import players, play_game

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/play-computer-vs-computer' methods=['POST'])
# def play_computer_vs_computer():

@app.route('/computer-vs-computer')
def computer_vs_computer():
    return render_template('computer-vs-computer.html', title="Computer Vs Computer", players=players)

# @app.route('/play-game', methods=['POST'])
# def play_game(player1, player2):
#     if player1.choice == "scissors" and player2.choice == "paper":
#         return player1
#     elif player1.choice == "scissors" and player2.choice == "rock":
#         return player2
#     elif player1.choice == "rock" and player2.choice == "scissors":
#         return player1
#     elif player1.choice == "rock" and player2.choice == "paper":
#         return player2
#     elif player1.choice == "paper" and player2.choice == "scissors":
#         return player2
#     elif player1.choice == "paper" and player2.choice == "rock":
#         return player1
