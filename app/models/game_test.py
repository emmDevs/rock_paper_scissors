import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.bob = Player("Bob", "scissors")
        self.alice = Player("Alice", "rock")
        self.janet = Player("Janet", "paper")
        self.game = Game(self.bob, self.alice)

    def test_game_has_a_player__player1(self):
        self.assertEqual("Bob", self.game.player1.name)

    def test_game_has_a_player__player2(self):
        self.assertEqual("Alice", self.game.player2.name)

    def test_play_game__scissors_vs_rock(self):
        self.game.play_game(self.bob, self.alice)
        self.assertEqual(self.alice, self.game.play_game(self.bob, self.alice))

    def test_play_game__scissors_vs_paper(self):
        self.game.play_game(self.bob, self.janet)
        self.assertEqual(self.bob, self.game.play_game(self.bob, self.janet))

