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
    if player1.choice == "scissors" and player2.choice == "paper":
        return f" {player1.name} chose {player1.choice}. {player2.name} chose {player2.choice}.  The winner is {player1.name}."
    elif player1.choice == "scissors" and player2.choice == "rock":
        return f" {player1.name} chose {player1.choice}. {player2.name} chose {player2.choice}.  The winner is {player2.name}."
    elif player1.choice == "rock" and player2.choice == "scissors":
        return player1.name
    elif player1.choice == "rock" and player2.choice == "paper":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "scissors":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "rock":
        return player1.name
    # winner = play_game(player1, player2)
    return render_template('computer-vs-computer.html', title="Computer Vs Computer", players=players, winner=play_game, player1=player1, player2=player2)


# @app.route('/play-game', <player1>, <player2)
# def play_game(player1, player2):
#     player1 = Player("Bob", "scissors")
#     player2 = Player("Alice", "rock")
#     winner = play_game()
#     # game=Game(player1, player2)
#     # # result = game.play_game()
#     return redirect('/computer-vs-computer', players=players, play_game=play_game(player1, player2))
 
