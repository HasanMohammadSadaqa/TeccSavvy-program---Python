"""Creating a class Logger with a method log() that prints out a message. Creating a decorator log_decorator that
applies the Logger class to a function by calling its log() method before and after the function is called. Apply the
decorator to a function and call the function."""


class Logger:
    def log(self, message):
        print(message)


logger = Logger()


def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        logger.log("Before calling function")
        print(original_function(*args, **kwargs))
        logger.log("After calling function")
        return original_function(*args, **kwargs)

    return wrapper


@log_decorator
def add_number(a, b):
    return a + b


result = add_number(2, 3)

