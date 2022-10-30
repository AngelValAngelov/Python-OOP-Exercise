from project.drink import Drink
from project.food import Food
from project.product import Product
# from inheritance_exercise.shop.project.drink import Drink
# from inheritance_exercise.shop.project.food import Food
# from inheritance_exercise.shop.project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        result = [p for p in self.products if p.name == product_name]
        if result:
            return result[0]
        return

    def remove(self, product_name):
        product = [p for p in self.products if p.name == product_name]
        if product:
            self.products.remove(product[0])

    def __repr__(self):
        return '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)
