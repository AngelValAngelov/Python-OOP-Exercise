class dictionary_iter:
    def __init__(self, dictionary_obj):
        self.dictionary_obj = dictionary_obj
        self.counter = 0
        self.len = len(self.dictionary_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.len:
            result = self.counter
            self.counter += 1
            return list(self.dictionary_obj.items())[result]
        raise StopIteration



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
