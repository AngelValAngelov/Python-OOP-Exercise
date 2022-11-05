# class IntegerList:
#     def __init__(self, *args):
#         self.list = [number for number in args]
#
#     def add(self, number):
#         if isinstance(number, int):
#             return self.list.append(number)
#         raise ValueError
#
#     def remove_index(self, number):
#         if isinstance(number, int):
#             self.list.remove(number)
#         raise IndexError
#
#     def get(self, number):
#         if len(self.list) < number:
#             return self.list[number]
#         raise IndexError
#
#     def insert(self, number):
#         if len(self.list) >= number:
#             raise IndexError
#         if not isinstance(number, int):
#             raise ValueError
#
#     def get_biggest(self):
#         return max(self.list)
#
#     def get_index(self, number):
#         return self.list.index(number)
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
        self.integers.list = []
        self.integers.add(1)
        self.assertEqual(self.integers.list, [1])


if __name__ == '__main__':
    unittest.main()
