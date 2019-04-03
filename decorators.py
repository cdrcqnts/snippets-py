# decorator function
def verbose(func):
    def wrapper(*args, **kwargs):
        print("Before", func.__name__)
        result = func(*args, **kwargs)
        print("After", func.__name__)
        return result
    return wrapper

# sample function


def hello(name):
    print('Hello', name)


# 2 ways to apply a decorator
# 1
hello = verbose(hello)


# 2
@verbose
def greet():
    """Doc from greet."""
    print('G\' day')

# @verbose is equal to:
# greet = verbose(greet)

# decorator function


def decorator(func_to_decorate):
    def wrapper(*args, **kwargs):
        # do something before invocation
        result = func_to_decorate(*args, **kwargs)
        # do something after
        return result
    wrapper.__doc__ = func_to_decorate.__doc__
    wrapper.__name__ = func_to_decorate.__name__
    return wrapper


# use case


@decorator
def greet2():
    """Doc from greet2."""
    print('G\' mornin\'')

# decorator class


class decorator_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # do something before invocation
        result = self.func(*args, **kwargs)
        # do something after
        return result

# use case


@decorator_class
def alaaf():
    # implementation
    print('Alaaf')


def
