def solution():
    def integers():
        counter = 0
        while True:
            counter += 1
            yield counter

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for num in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

