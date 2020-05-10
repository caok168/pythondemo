
def gen_func():
    try:
        yield "http://projectedu.com"
    except GeneratorExit:
        pass
    yield 2
    yield 3
    return "ck"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    # next(gen)


# GeneratorExit 是继承自 BaseException，Exception
