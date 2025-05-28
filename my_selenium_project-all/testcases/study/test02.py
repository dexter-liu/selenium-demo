# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'wrapper of decorator')
#         func(*args, **kwargs)
#     return wrapper
#
#
# @my_decorator
# def greet(message):
#     print(message)
#
#
# greet('hello world')


def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(3)
def greet(message):
    print(message)

greet('hello, world')