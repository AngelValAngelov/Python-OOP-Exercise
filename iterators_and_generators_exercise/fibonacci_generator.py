def fibonacci():
    a, b = 0, 1
    for _ in range(100000):
        yield a
        a, b = b, a + b


generator = fibonacci()
for i in range(5):
    print(next(generator))
