from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name=family_name, budget=salary_one+salary_two, members_count=2*len(self.children))
        self.children = [ch for ch in children]
        self.appliances = [TV(), Fridge(), Laptop(), TV(), Fridge(), Laptop()]
        self.appliances.append([ch for ch in self.children])
        self.calculate_expenses(self.appliances)