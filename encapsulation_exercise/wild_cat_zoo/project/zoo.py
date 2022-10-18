from collections import defaultdict
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) + 1 <= self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) + 1 <= self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            self.workers.remove(worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        if sum([w.salary for w in self.workers]) <= self.__budget:
            self.__budget -= sum([w.salary for w in self.workers])
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        if sum([a.money_for_care for a in self.animals]) <= self.__budget:
            self.__budget -= sum([a.money_for_care for a in self.animals])
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_by_type = defaultdict(list)
        print(animals_by_type)
        for a in self.animals:
            animals_by_type[a.__class__.__name__].append(a)

        return '\n'.join([
                             f'You have {len(self.animals)} animals',
                             f'----- {len(animals_by_type["Lion"])} Lions:'
                         ] + [
                             repr(lion) for lion in animals_by_type['Lion']
                         ] + [
                             f'----- {len(animals_by_type["Tiger"])} Tigers:'
                         ] + [
                             repr(tiger) for tiger in animals_by_type['Tiger']
                         ] + [
                             f'----- {len(animals_by_type["Cheetah"])} Cheetahs:'
                         ] + [
                             repr(cheetah) for cheetah in animals_by_type['Cheetah']
                         ])

    def workers_status(self):
        workers_by_type = defaultdict(list)
        for w in self.workers:
            workers_by_type[w.__class__.__name__].append(w)

        return '\n'.join([
                             f'You have {len(self.workers)} workers',
                             f'----- {len(workers_by_type["Keeper"])} Keepers:'
                         ] + [
                             repr(w) for w in workers_by_type['Keeper']
                         ] + [
                             f'----- {len(workers_by_type["Caretaker"])} Caretakers:'
                         ] + [
                             repr(w) for w in workers_by_type['Caretaker']
                         ] + [
                             f'----- {len(workers_by_type["Vet"])} Vets:'
                         ] + [
                             repr(w) for w in workers_by_type['Vet']
                         ])


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
