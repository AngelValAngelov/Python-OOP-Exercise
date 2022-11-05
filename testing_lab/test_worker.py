class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


import unittest


class TestWorker(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('Angel', 100, 10)

    def test_initialise_vehicle(self):
        self.assertEqual('Angel', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_worker_energy_expect_increment_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_worker_energy_is_less_than_zero_expect_raise_exception(self):
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_energy_is_equal_to_zero_expect_raise_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_expect_increase_salary_after_work(self):
        self.worker.money = 0
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_worker_expect_decrease_energy_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_worker_expect_return_correct_result(self):
        self.worker.get_info()
        result = 'Angel has saved 0 money.'
        self.assertEqual(self.worker.get_info(), result)


if __name__ == '__main__':
    unittest.main()
