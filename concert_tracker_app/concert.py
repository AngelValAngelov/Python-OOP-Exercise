class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if value not in ["Metal", "Rock", "Jazz"]:
            raise ValueError(f"Our group doesn't play {value}!")
        self._genre = value

    @property
    def audience(self):
        return self._audience

    @audience.setter
    def audience(self, value):
        if value < 1:
            raise ValueError("At least one person should attend the concert!")
        self._audience = value

    @property
    def ticket_price(self):
        return self._ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        if value < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")
        self._ticket_price = value

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0.00:
            raise ValueError("Expenses cannot be a negative number!")
        self._expenses = value

    @property
    def place(self):
            return self._place

    @place.setter
    def place(self, value):
        if len(value) < 2 or value.isspace():
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        self._place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
