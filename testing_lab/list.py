class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.integers = IntegerList()

    def test_initialization_IntegerList(self):
        self.integers.list = [1, 2, 3]
        self.assertEqual(self.integers.list, [1, 2, 3])

    def test_add_expect_raise_error_if_the_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.integers.add(1.1)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_expect_add_integer_to_the_list(self):
        self.assertEqual(self.integers.add(1), [1])

    def test_remove_expect_raise_error_if_the_element_is_bigger_than_length_of_the_list(self):
        with self.assertRaises(IndexError) as ex:
            self.integers.remove_index(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_expect_remove_the_index_integer(self):
        self.integers.add(1)
        self.assertEqual(self.integers.remove_index(0), 1)

    def test_get_integer_expect_raise_error_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.integers.get(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_integer_expect_return_correct_integer(self):
        self.integers.add(2)
        self.assertEqual(self.integers.get(0), 2)

    def test_insert_integer_expect_raise_error_if_the_element_is_bigger_than_length_of_the_list(self):
        self.integers.add(1)
        with self.assertRaises(IndexError) as ex:
            self.integers.insert(5, 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_integer_expect_raise_error_if_integer_is_different_type(self):
        self.integers.add(1)
        with self.assertRaises(ValueError) as ex:
            self.integers.insert(0, 1.1)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_integer_expect_insert_correctly_integer_to_the_integer_list(self):
        self.integers.add(1)
        self.integers.add(2)
        self.integers.add(3)
        self.integers.insert(0, 11)
        self.assertEqual(self.integers.get_data(), [11, 1, 2, 3])

    def test_get_biggest_expect_return_biggest_integer_of_the_integer_list(self):
        self.integers.add(1)
        self.integers.add(2)
        self.integers.add(3)
        self.assertEqual(self.integers.get_biggest(), 3)

    def test_get_index_expect_return_correct_index_of_the_integer(self):
        self.integers.add(1)
        self.integers.add(2)
        self.integers.add(3)
        self.assertEqual(self.integers.get_index(2), 1)


if __name__ == '__main__':
    unittest.main()
