def validar_numeros(func):
    def wrapper(*args, **kwargs):
        # Validar argumentos posicionales
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argumento inválido: {arg} no es un número")

        # Validar argumentos nombrados
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Argumento inválido: {key}={value} no es un número")

        return func(*args, **kwargs)

    return wrapper
