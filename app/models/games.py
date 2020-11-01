from app.models.game import *
from app.models.player import *

bob = Player("Bob", "scissors")
alice = Player("Alice", "rock")
# janet = Player("Janet", "paper")
game = Game(bob, alice)

players = (bob, alice)

def play_game(player1, player2):
    if player1.choice == "scissors" and player2.choice == "paper":
        return player1.name
    elif player1.choice == "scissors" and player2.choice == "rock":
        return player2.name
    elif player1.choice == "rock" and player2.choice == "scissors":
        return player1.name
    elif player1.choice == "rock" and player2.choice == "paper":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "scissors":
        return player2.name
    elif player1.choice == "paper" and player2.choice == "rock":
        return player1.name
    



