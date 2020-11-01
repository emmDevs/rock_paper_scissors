class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2 

    # self.bob = Player("Bob", "scissors")
    # self.alice = Player("Alice", "rock")
    # # self.janet = Player("Janet", "paper")
    # self.game = Game(self.bob, self.alice)

    # def play_game(self):
    #     if self.player1.choice == "scissors" and self.player2.choice == "paper":
    #         return self.player1
    #     elif self.player1.choice == "scissors" and self.player2.choice == "rock":
    #         return self.player2
    #     elif self.player1.choice == "rock" and self.player2.choice == "scissors":
    #         return self.player1
    #     elif self.player1.choice == "rock" and self.player2.choice == "paper":
    #         return self.player2
    #     elif self.player1.choice == "paper" and self.player2.choice == "scissors":
    #         return self.player2
    #     elif self.player1.choice == "paper" and self.player2.choice == "rock":
    #         return self.player1
