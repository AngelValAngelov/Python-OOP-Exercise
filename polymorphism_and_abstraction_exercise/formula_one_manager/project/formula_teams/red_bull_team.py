from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)
        self.expenses = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            revenue = 1500000 + 20000 - 250000
            self.budget += revenue
        elif race_pos == 2:
            revenue = 800000 + 20000 - 250000
            self.budget += revenue
        elif race_pos == 3 or race_pos == 4 or race_pos == 5 or race_pos == 6 or race_pos == 7:
            revenue = 20000 - 250000
            self.budget += revenue
        elif race_pos == 8:
            revenue = 20000 - 250000
            self.budget += revenue
        elif race_pos == 9:
            revenue = 10000 - 250000
            self.budget += revenue
        elif race_pos == 10:
            revenue = 10000 - 250000
            self.budget += revenue
        else:
            revenue = -250000
            self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


