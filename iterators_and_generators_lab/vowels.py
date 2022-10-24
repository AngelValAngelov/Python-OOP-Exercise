class vowels:
    def __init__(self, text: str):
        self.text = text
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        while self.index < len(self.text) - 1:
            self.index += 1
            if self.text[self.index].lower() in 'a,e,i,u,y,o':
                return self.text[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
