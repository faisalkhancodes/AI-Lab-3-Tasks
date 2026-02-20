import random

def random_numbers():
    for _ in range(5):
        yield random.randint(1, 100)

for num in random_numbers():
    print(num)