from itertools import permutations


def possible_permutations(numbers):
    for arg in permutations(numbers):
        yield list(arg)


[print(n) for n in possible_permutations([1, 2, 3])]
