from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        capacity = 15
        return capacity

    @staticmethod
    def customer_capacity():
        capacity = 10
        return capacity

    def add_customer(self, customer: Customer):
        if MovieWorld.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if MovieWorld.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id]
        dvd = [d for d in self.dvds if d.id == dvd_id]

        customer_name = customer[0].name
        dvd_name = dvd[0].name
        dvd_age_restriction = dvd[0].age_restriction

        if dvd[0] in customer[0].rented_dvds:
            return f"{customer_name} has already rented {dvd_name}"
        if dvd[0].is_rented:
            return "DVD is already rented"
        if customer[0].age < dvd[0].age_restriction:
            return f"{customer_name} should be at least {dvd_age_restriction} to rent this movie"

        customer[0].rented_dvds.append(dvd[0])
        dvd[0].is_rented = True
        return f"{customer_name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c for c in self.customers if c.id == customer_id]
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id]
        if dvd[0] in customer[0].rented_dvds:
            dvd[0].is_rented = False
            customer[0].rented_dvds.remove(dvd[0])
            return f"{customer[0].name} has successfully returned {dvd[0].name}"
        return f"{customer[0].name} does not have that DVD"

    def __repr__(self):
        customer = '\n'.join([n.__repr__() for n in self.customers])
        dvds = '\n'.join([d.__repr__() for d in self.dvds])

        result = customer + '\n' + dvds
        return result


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
