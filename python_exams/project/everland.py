from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        return f'Monthly consumtions: {sum([r.expenses for r in self.rooms]) + sum([r.room_cost for r in self.rooms])}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses:
                room.budget -= room.expenses + room.room_cost
                result.append(
                    f"{room.family_name} paid {room.expenses + room.room_cost}$ and have {room.budget}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        result = [f'Total population: {sum([x.members_count for x in self.rooms])}']
        for room in self.rooms:
            result.append(
                f'{room.family_name} with {room.members_count} members. Budget: {room.budget}$, Expenses: {room.expenses}$')
            if room.__class__.__name__ == 'YoungCoupleWithChildren':
                child_number = 0
                for child in room.children:
                    child_number += 1
                    result.append(f'--- Child {child_number} monthly cost: {child.get_monthly_expense()}$')
            if hasattr(room, "appliances"):
                result.append(f'--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances])}$')
        return '\n'.join(result)


from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child

everland = Everland()


def test_one():
    young_couple = YoungCouple("Johnsons", 150, 205)

    child1 = Child(5, 1, 2, 1)
    child2 = Child(3, 2)
    young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

    everland.add_room(young_couple)
    everland.add_room(young_couple_with_children)

    print(everland.get_monthly_consumptions())
    print(everland.pay())
    print(everland.status())


if __name__ == "__main__":
    test_one()
