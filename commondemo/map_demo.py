lis = [1, 2, 3, 4, 5]


def fn(x):
    return x**2


res = map(fn, lis)
print(res)

res = [i for i in res if i > 10]
print(res)


def square(x):
    return x ** 2


res = map(square, [1, 2, 3, 4, 5])
print(res)
res = [x for x in res]
print(res)

res = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(res)
res = [x for x in res]
print(res)

res = map(lambda x, y: x+y, [1, 3, 5, 7, 9], [2, 4, 6, 8,10])
print(res)
res = [x for x in res]
print(res)


def add100(x):
    return x + 100

list1 = [11, 22, 33]
res = map(add100, list1)
res = [x for x in res]
print(res)

#######
list1 = [11, 22, 33]
res = map(None, list1)
res = [x for x in res]
print(res)

