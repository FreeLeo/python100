# 函数的使用方式 https://github.com/jackfrued/Python-100-Days/blob/master/Day16-20/16-20.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md
from functools import wraps
from time import time


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time() - start}秒")
        return result
    return wrapper


def record(output):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            output(f"{func.__name__}: {time() - start}秒")
            return result
        return wrapper
    return decorate


def add(x, y):
    return x+y


def perform_add(add_func, x, y):
    return add_func(x, y)


def return_add_func():
    return add


def sum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def custom_print(str):
    print(f"lizhen : {str}")


@record(custom_print)
def create_dict(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


@record_time
def test_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)


def main():
    # total = add
    # print(total(1, 1))
    # print(perform_add(total, 1, 1))
    # add_func = return_add_func()
    # print(add_func(2, 2))

    # items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    # items2 = [x ** 2 for x in range(1, 10) if x % 2]

    print(sum(1, 1, 1, 1))
    create_dict(name="Alice", age=30, city="New York")
    test_args(1, 1, 1, name="Alice", age=30, city="New York")


if __name__ == '__main__':
    main()
