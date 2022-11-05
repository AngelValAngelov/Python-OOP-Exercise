class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Pesho')

    def test_cat_initialisation(self):
        self.assertEqual(self.cat.name, 'Pesho')

    def test_cat_expect_size_increase_in_eat_method(self):
        self.cat.size = 0
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_expect_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)

    def test_cat_expect_raise_error_if_try_to_feed_again(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_expect_raise_error_if_cat_try_to_asleep_if_is_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_expect_not_sleep_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
