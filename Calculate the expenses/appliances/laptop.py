from project.appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self):
        super(Laptop, self).__init__(1)
