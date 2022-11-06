import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(15.5, 100.5)

    def test_initialization_vehicle(self):
        self.assertEqual(self.vehicle.fuel, 15.5)
        self.assertEqual(self.vehicle.horse_power, 100.5)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_expect_raise_error_if_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_expect_decrease_fuel_correctly(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 3)

    def test_refuel_expect_raise_error_if_fuel_is_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_expect_work_correctly(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 4)

    def test_str_method(self):
        car = str(self.vehicle)
        self.assertEqual("The vehicle has 100.5 horse power with 15.5 fuel left and 1.25 fuel consumption", car)


if __name__ == '__main__':
    unittest.main()
