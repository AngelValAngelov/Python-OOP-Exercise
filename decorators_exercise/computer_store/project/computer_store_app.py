
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self,):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer != "Desktop Computer" and type_computer != "Laptop":
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Desktop Computer":
            new_computer = DesktopComputer(manufacturer, model)
            self.warehouse.append(new_computer)
            return new_computer.configure_computer(processor, ram)
        new_laptop = Laptop(manufacturer, model)
        self.warehouse.append(new_laptop)
        return new_laptop.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += (client_budget - computer.price)
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")



computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
