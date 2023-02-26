from abc import ABC, abstractmethod


class Musician(ABC):
    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills: list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '' or value.isspace():
            raise ValueError("Musician name cannot be empty!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self._age = value

    def learn_new_skill(self, new_skill: str):
        pass
