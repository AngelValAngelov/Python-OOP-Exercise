class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name: str = name
        self.budget: float = budget
        self.members_count: int = members_count
        self.children: list = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        self.expenses = sum([a.get_monthly_expense() for c in args for a in c])
