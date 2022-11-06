class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(2010, 'Opel', 10, 100)

    def test_initialization_Car(self):
        self.assertEqual(self.car.make, 2010)
        self.assertEqual(self.car.model, 'Opel')
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 100)

    def test_make_method_expect_return_new_value(self):
        self.car.make = 2000
        self.assertEqual(self.car.make, 2000)

    def test_make_expect_raise_error_if_new_value_is_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_method_expect_return_new_value(self):
        self.car.model = 'VW'
        self.assertEqual(self.car.model, 'VW')

    def test_model_expect_raise_error_if_new_value_is_invalid(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_less_than_zero_expect_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_expect_return_new_value(self):
        self.car.fuel_consumption = 5
        self.assertEqual(self.car.fuel_consumption, 5)

    def test_fuel_capacity_expect_raise_error_if_new_value_is_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_expect_return_new_value(self):
        self.car.fuel_capacity = 50
        self.assertEqual(self.car.fuel_capacity, 50)

    def test_fuel_amount_expect_raise_error_if_new_value_is_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_expect_raise_error_if_value_is_less_than_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_expect_fuel_amount_increase_with_fuel_value(self):
        self.car.fuel_amount = 0
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_method_expect_refuel_more_than_fuel_capacity_fuel_amount_should_be_equal_to_fuel_capacity(self):
        self.car.fuel_amount = 0
        self.car.refuel(150)
        self.assertEqual(self.car.fuel_amount, 100)

    def test_drive_method_expect_raise_error_if_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_expect_return_fuel_left_after_drive(self):
        self.car.fuel_amount = 100
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 90)


if __name__ == '__main__':
    unittest.main()
