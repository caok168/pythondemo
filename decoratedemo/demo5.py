import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name,message):
    print("hello ,{},{}".format(name,message))


greet('ck','come on')

print(greet.__name__)