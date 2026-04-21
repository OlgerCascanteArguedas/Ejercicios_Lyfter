from datetime import date
from functools import wraps

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth  # expected type: datetime.date

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year

        # Adjust if birthday has not occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1

        return years

def adult_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = None

        # Look for a User instance in positional arguments
        for arg in args:
            if isinstance(arg, User):
                user = arg
                break

        # Look for a User instance in keyword arguments
        if not user:
            for value in kwargs.values():
                if isinstance(value, User):
                    user = value
                    break

        if not user:
            raise ValueError("No User instance found in arguments")

        if user.age < 18:
            raise PermissionError("User must be at least 18 years old")

        return func(*args, **kwargs)

    return wrapper
