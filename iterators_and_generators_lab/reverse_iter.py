class reverse_iter:
    def __init__(self, numbers: list):
        self.numbers = numbers
        self.index = len(self.numbers)

    def __iter__(self):
        return self

    def __next__(self):
        while self.index > 0:
            self.index -= 1
            return self.numbers[self.index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
