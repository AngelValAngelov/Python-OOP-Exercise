from project.appliances.appliance import Appliance


class TV(Appliance):
    def __init__(self):
        super(TV, self).__init__(1.5)
