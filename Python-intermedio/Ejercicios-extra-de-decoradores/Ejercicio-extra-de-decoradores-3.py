from datetime import datetime
from functools import wraps


def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Todos los argumentos deben ser numéricos")
        return func(*args, **kwargs)
    return wrapper


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        now = datetime.now()
        args_str = ", ".join(str(arg) for arg in args)
        print(f"func:{func.__name__} - args: {args_str} - [{now}] - Resultado: {result}")
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b):
    return a * b
