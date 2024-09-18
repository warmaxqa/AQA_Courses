# 1 A decorator that logs the arguments and results of a called function:

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"The function is called: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_decorator
def add(a, b):
    return a + b


add(3, 5)


# 2 A decorator who overhauls and picks up the problems that arise during the execution of the function:

def exception_handler_decorator(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"A runtime error occurred {func.__name__}: {e}")

            return None

    return wrapper


@exception_handler_decorator
def divide(a, b):
    return a / b

divide(10, 2)
divide(10, 0)
