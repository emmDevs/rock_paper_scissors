class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2 

    def play_game(self, player1, player2):
        if player1.choice == "scissors" and player2.choice == "paper":
            return player1
        elif player1.choice == "scissors" and player2.choice == "rock":
            return player2
        elif player1.choice == "rock" and player2.choice == "scissors":
            return player1
        elif player1.choice == "rock" and player2.choice == "paper":
            return player2
        elif player1.choice == "paper" and player2.choice == "scissors":
            return player2
        elif player1.choice == "paper" and player2.choice == "rock":
            return player1
