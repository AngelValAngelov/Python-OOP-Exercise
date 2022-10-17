from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number]
        if room and room[0].capacity >= people and room[0].is_taken == False:
            self.guests += people
            room[0].take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number]
        if room:
            self.guests -= room[0].guests
            room[0].free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if r.is_taken == False]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r) for r in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(r) for r in taken_rooms])}"


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
