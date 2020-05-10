
def fib(to=10):
    curr = 0
    next = 1
    count = 0
    while count < to:
        yield curr
        curr = next
        next = curr + next
        count += 1

if __name__ == "__main__":
    # for x in fib():
    #     print(x+1)
    x = fib()
    print(x.send())
