import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("BEFORE executing func")
        func()
        print("AFTER executing func")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I am the function!")


# my_function()


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("BEFORE executing func")
            if number == 57:
                print("NOT running the function.")
            else:
                func(*args, **kwargs)
            print("AFTER executing func")
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_function_too(x, y):
    print(x + y)


my_function_too(57, 67)
