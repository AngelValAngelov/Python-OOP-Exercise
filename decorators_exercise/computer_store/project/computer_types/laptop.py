from project.computer_types.computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        available_processors = {'AMD Ryzen 9 5950X': 900,
                                'Intel Core i9-11900H': 1050,
                                'Apple M1 Pro': 1200}
        available_rams = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600}

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in available_rams:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.price = available_processors[processor] + available_rams[ram]
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
