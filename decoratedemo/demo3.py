
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
        print('end of wrapper of decorator')
    return wrapper

@my_decorator
def greet():
    print('hello world')

# greet = my_decorator(greet)
#
greet()