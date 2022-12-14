class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_number = -self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            self.current_number += self.step
            return self.current_number
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
