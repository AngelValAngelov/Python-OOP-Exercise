from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            revenue = 1000000 + 100000 - 200000
            self.budget += revenue
        elif race_pos == 2:
            revenue = 500000 + 100000 - 200000
            self.budget += revenue
        elif race_pos == 3:
            revenue = 500000 + 100000 - 200000
            self.budget += revenue
        elif race_pos == 4:
            revenue = 100000 - 200000
            self.budget += revenue
        elif race_pos == 5:
            revenue = 100000 - 200000
            self.budget += revenue
        elif race_pos == 6:
            revenue = 50000 - 200000
            self.budget += revenue
        elif race_pos == 7:
            revenue = 50000 - 200000
            self.budget += revenue
        else:
            revenue = -200000
            self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
