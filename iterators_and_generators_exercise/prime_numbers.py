def get_primes(*args):
    for arg in args:
        for el in arg:
            if el < 2:
                continue
            else:
                if el % 2 != 0 and el % 3 != 0 or el == 2 or el == 2 or el == 3:
                    yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
