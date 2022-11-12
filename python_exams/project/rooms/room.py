class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children: list = []
        self.expenses = 0

    def calculate_expenses(self, *args):
        return sum([el for l in args for el in l]) * 30

