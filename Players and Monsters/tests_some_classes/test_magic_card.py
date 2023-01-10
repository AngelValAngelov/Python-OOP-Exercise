import unittest

from project.card.magic_card import MagicCard


class testMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard('Power')

    def test_magic_card_attributes(self):
        self.assertEqual(self.card.name, 'Power')
        self.assertEqual(self.card.damage_points, 5)
        self.assertEqual(self.card.health_points, 80)

    def test_if_name_is_empty_string_raise_error(self):
        with self.assertRaises(ValueError) as cm:
            self.card.name = ''
        self.assertEqual(str(cm.exception), "Card's name cannot be an empty string.")

    def test_damage_point_should_raise_error_if_points_are_below_than_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.card.damage_points = -1
        self.assertEqual(str(cm.exception), "Card's damage points cannot be less than zero.")

    def test_health_point_should_raise_error_if_points_are_below_than_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.card.health_points = -1
        self.assertEqual(str(cm.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
