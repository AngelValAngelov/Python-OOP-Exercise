import unittest

from project.rooms.room import Room


class TestRoomClass(unittest.TestCase):
    def setUp(self):
        self.room = Room('Angelov', 100, 1)

    def test_initialization(self):
        self.assertEqual(self.room.family_name, 'Angelov')
        self.assertEqual(self.room.budget, 100)
        self.assertEqual(self.room.members_count, 1)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_negative_expenses_should_raise_value_error(self):
        with self.assertRaises(ValueError) as cm:
            self.room.expenses = -1
        self.assertEqual(str(cm.exception), "Expenses cannot be negative")


if __name__ == '__main__':
    unittest.main()
