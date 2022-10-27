def vowel_filter(func):
    def wrapper():
        return [l for l in func() if l in {'a', 'e', 'i', 'o', 'u', 'y'}]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
