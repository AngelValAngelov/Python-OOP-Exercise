from project.player.advanced import Advanced
import unittest


class testAdvancedPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Advanced('Toto')

    def test_validate_player_attributes(self):
        self.assertEqual(self.player.username, 'Toto')
        self.assertEqual(self.player.health, 250)
        self.assertEqual(self.player.card_repository.__class__.__name__, "CardRepository")

    def test_empty_username_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.username = ''
        self.assertEqual(str(cm.exception), "Player's username cannot be an empty string.")

    def test_less_than_zero_player_health_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.health = -1
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")

    def test_less_than_zero_player_damage_should_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.player.take_damage(-1)
        self.assertEqual(str(cm.exception), "Damage points cannot be less than zero.")

    def test_health_points_decrease_with_damage_points(self):
        self.player.take_damage(10)
        self.assertEqual(self.player.health, 240)

    def test_is_dead_should_return_true_if_player_health_is_equal_or_less_than_zero(self):
        self.player.health = -1
        self.assertTrue(self.player.is_dead)

    def test_is_dead_should_return_false_if_player_health_is_more_than_zero(self):
        self.player.health = 1
        self.assertFalse(self.player.is_dead)


if __name__ == "__main__":
    unittest.main()
