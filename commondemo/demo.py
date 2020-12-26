from functools import partial
import random


def multiply(x, y):
    return x - y


print(multiply(2, 3))
print(multiply(3, 4))


def double(x, y=2):
    return multiply(x, y)


print(double(3))

double = partial(multiply, 2)
print(double(16))

gap = partial(random.randint, 1, 15)
for i in range(5):
    print(gap())
