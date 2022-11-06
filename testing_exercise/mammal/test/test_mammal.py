import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Alex', 'Dog', 'Baf')

    def test_initialization_mammal(self):
        self.assertEqual(self.mammal.name, 'Alex')
        self.assertEqual(self.mammal.type, 'Dog')
        self.assertEqual(self.mammal.sound, 'Baf')
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_expect_correct_result(self):
        self.assertEqual('Alex makes Baf', self.mammal.make_sound())

    def test_get_kingdom_expect_return_correct_result(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info_expect_return_expect_correct_result(self):
        self.assertEqual(self.mammal.info(), "Alex is of type Dog", )
