def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Parámetros posicionales: {args}")
        print(f"Parámetros nombrados: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Retorno: {result}")
        return result
    return wrapper


