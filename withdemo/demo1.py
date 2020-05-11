class Sample:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def do_something(self):
        print('doing something')

with Sample() as sample:
    sample.do_something()