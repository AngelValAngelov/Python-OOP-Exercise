class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count < self.number:
            result = self.sequence[self.count % len(self.sequence)]
            self.count += 1
            return result
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
