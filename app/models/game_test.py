import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.bob = Player("Bob", "scissors")
        self.alice = Player("Alice", "rock")
        self.game = Game(self.bob, self.alice)

    def test_game_has_a_player__player1(self):
        self.assertEqual("Bob", self.game.player1.name)

    def test_game_has_a_player__player2(self):
        self.assertEqual("Alice", self.game.player2.name)