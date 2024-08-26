def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


@logger
def multiply(a, b):
    return a * b


print(add(100, 223))
print(multiply(23, 4))
