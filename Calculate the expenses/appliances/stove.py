from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super(Stove, self).__init__(0.7)
