def infinite_even_numbers():
    number = 0
    while True:
        yield number
        number += 2

evens = infinite_even_numbers()

for _ in range(5):
    print(next(evens))
