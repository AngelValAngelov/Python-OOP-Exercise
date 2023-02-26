from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        if name in [n.name for n in self.musicians]:
            raise Exception(f"{name} is already a musician!")
        if musician_type == "Singer":
            self.musicians.append(Singer(name, age))
        elif musician_type == "Drummer":
            self.musicians.append(Drummer(name, age))
        elif musician_type == "Guitarist":
            self.musicians.append(Guitarist(name, age))
        # errors
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [band.name for band in self.bands]:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = [c for c in self.concerts if c.place == place]
        if concert:
            raise Exception(f"{concert[0].place} is already registered for {concert[0].genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")
        if band_name not in [band.name for band in self.bands]:
            raise Exception(f"{band_name} isn't a band!")
        musician = [m for m in self.musicians if m.name == musician_name][0]
        band = [b for b in self.bands if b.name == band_name][0]
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        current_band = [b for b in self.bands if b.name == band_name]
        if not current_band:
            raise Exception(f"{band_name} isn't a band!")
        member = [m for m in current_band[0].members if m.name == musician_name]
        if not member:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        current_band[0].members.remove(member[0])
        return f"{member[0].name} was removed from {current_band[0].name}."

    def start_concert(self, concert_place: str, band_name: str):
        drummer = 0
        singer = 0
        guitarist = 0

        band = [b for b in self.bands if b.name == band_name][0]
        for member in band.members:
            if member.__class__.__name__ == 'Drummer':
                drummer += 1
            elif member.__class__.__name__ == 'Singer':
                singer += 1
            elif member.__class__.__name__ == 'Guitarist':
                guitarist += 1

        if drummer == 0 or singer == 0 or guitarist == 0:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        drummer_rock = False
        singer_rock = False
        guitarist_rock = False

        drummer_metal = False
        singer_metal = False
        guitarist_metal = False

        drummer_jazz = False
        singer_jazz = False
        guitarist_jazz = False

        for member in band.members:
            if member.__class__.__name__ == 'Drummer':
                if [s for s in member.skills if s == 'play the drums with drumsticks']:
                    drummer_rock = True
                if [s for s in member.skills if s == 'play the drums with drumsticks']:
                    drummer_metal = True
                if [s for s in member.skills if s == 'play the drums with drum brushes']:
                    drummer_jazz = True
            if member.__class__.__name__ == 'Singer':
                if [s for s in member.skills if s == 'sing high pitch notes']:
                    singer_rock = True
                if [s for s in member.skills if s == 'sing low pitch notes']:
                    singer_metal = True
                if [s for s in member.skills if s == 'sing high pitch notes'] and [s for s in member.skills if s == 'sing low pitch notes']:
                    singer_jazz = True
            if member.__class__.__name__ == 'Guitarist':
                if [s for s in member.skills if s == 'play rock']:
                    guitarist_rock = True
                if [s for s in member.skills if s == 'play metal']:
                    guitarist_metal = True
                if [s for s in member.skills if s == 'play jazz']:
                    guitarist_jazz = True

        rock_concert = [g for g in self.concerts if g.genre == 'Rock']
        metal_concert = [g for g in self.concerts if g.genre == 'Metal']
        jazz_concert = [g for g in self.concerts if g.genre == 'Jazz']
        if rock_concert:
            if drummer_rock and singer_rock and guitarist_rock:
                concert = rock_concert[0]
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        if metal_concert:
            if drummer_metal and singer_metal and guitarist_metal:
                concert = metal_concert[0]
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        if jazz_concert:
            if drummer_jazz and singer_jazz and guitarist_jazz:
                concert = jazz_concert[0]
                profit = (concert.audience * concert.ticket_price) - concert.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

# musician_types = ["Singer", "Drummer", "Guitarist"]
# names = ["George", "Alex", "Lilly"]
#
# app = ConcertTrackerApp()
#
# for i in range(3):
#     print(app.create_musician(musician_types[i], names[i], 20))
#
# print(app.musicians[0].learn_new_skill("sing high pitch notes"))
# print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
# print(app.musicians[2].learn_new_skill("play rock"))
#
# print(app.create_band("RockName"))
# for i in range(3):
#     print(app.add_musician_to_band(names[i], "RockName"))
#
# # print(app.remove_musician_from_band('George', 'RockName'))
#
# print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))
#
# print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
# print(app.start_concert("Sofia", "RockName"))
