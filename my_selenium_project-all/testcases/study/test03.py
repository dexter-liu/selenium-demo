class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Function {self.func.__name__} has been called {self.num_calls} times')
        return self.func(*args, **kwargs)


@Count
def example():
    print('hello, world')

example()
example()

