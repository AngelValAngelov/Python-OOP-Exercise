class Band:
    members = []

    def __init__(self, name: str):
        self.name = name
        # self.members = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Band name should contain at least one character!")
        self._name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."




