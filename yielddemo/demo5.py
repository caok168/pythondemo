
def h():
    print('Wen Chuan')
    m = yield 5
    print(m)
    d = yield 12
    print('We are together!')

c = h()
# print(next(c))
next(c)
print(c.send('Fighting!'))

