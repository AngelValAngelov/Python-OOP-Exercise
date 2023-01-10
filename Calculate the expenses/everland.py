from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = sum([r.calculate_expenses() for r in self.rooms])
        return f"Monthly consumption: {result}$."

    def pay(self):
        for room in self.rooms:
            if room.expenses <= room.budget:
                room.budget -= room.expenses
                return f"{room.family_name} paid {room.expenses}$ and have {room.budget}$ left."
            else:
                self.rooms.remove(room)
                return f"{room.family_name} does not have enough budget and must leave the hotel."

    def status(self):
        pass

