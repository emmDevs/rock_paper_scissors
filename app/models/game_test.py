import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.bob = Player("Bob", "scissors")
        self.alice = Player("Alice", "rock")
        self.game = Game(self.bob, self.alice)

