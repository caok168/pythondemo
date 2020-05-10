def addlist(alist):
    for i in alist:
        yield i + 1

alist = [1,2,3,4]
for x in addlist(alist):
    print(x)

print('*'*20)

def h():
    print('To be brave')
    yield 5

c = h()
print(next(c))


for i in range(5):
    pass