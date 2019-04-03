import functools


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (23, 45, 57, 78, 23, 1, 3)

    def getName(self):
        print(self.name)


player = LotteryPlayer("Rolf")
player.getName()


def bla():
    a_list = [1, 2, 3, 4, 5]
    return list(filter(lambda x: x % 2 == 0, a_list))


print(bla())


# --- DECORATOR --->
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator BEFORE func is executed.")
        func()
        print("In the decorator AFTER func is executed.")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function!")

# my_function()


# --- DECORATOR WITH ARGUMENTS --->
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator BEFORE func is executed.")
            if (number == 54):
                print("Not running the function! Number is 54.")
            else:
                func(*args, **kwargs)
            print("In the decorator AFTER func is executed.")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(57)
def my_function_too(x, y):
    print(x + y)


my_function_too(57, 67)
