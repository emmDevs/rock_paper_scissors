import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.bob = Player("Bob", "scissors")
        self.alice = Player("Alice", "rock")

    def test_player_has_a_name(self):
        self.assertEqual("Bob", self.bob.name)