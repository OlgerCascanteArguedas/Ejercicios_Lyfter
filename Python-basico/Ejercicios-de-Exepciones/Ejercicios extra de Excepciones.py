def main():
    while True:
        name = input("Ingrese su nombre: ")
        if name.isdigit():
            print("El nombre no puede ser un número. Intente nuevamente.")
        elif name.strip() == "":
            print("El nombre no puede estar vacío. Intente nuevamente.")
        else:
            break
    while True:
        age_input = input("Ingrese su edad: ")
        if not age_input.isdigit():
            print("Edad no válida. Ingrese solo números.")
        else:
            age = int(age_input)
            break
    print(f"Hola {name}, su edad es {age}")
    #name = input("Ingrese su nombre: ")
    #if name.isdigit():
    #    raise ValueError("El nombre no puede ser un número")
    #age_input = input("Ingrese su edad: ")
    #if not age_input.isdigit():
    #    raise ValueError("Número no valido")
    #age = int(age_input)
    #print(f"Hola {name}, su edad es {age}")
if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(error)
#########################
def convert_to_integer(lista):
    print("Resultado:")
    for element in lista:
        try:
            number = int(element)
            print(f"{element} convertido a {number}")
        except ValueError:
            print(f"No se pudo convertir el elemento: {element}")
########################
def sum_values(lista):
    total = 0.0
    for element in lista:
        try:
            number = float(element)
            total += number
            print(f"{number} sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {element}")
    print("Total de la suma:", total)
