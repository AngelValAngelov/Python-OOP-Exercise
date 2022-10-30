from project.product import Product
# from inheritance_exercise.shop.project.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, quantity=10)
