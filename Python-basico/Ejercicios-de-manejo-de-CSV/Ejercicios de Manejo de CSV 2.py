import csv
import os
def ask_number():
    while True:
        try:
            n = int(input("¿Cuántos videojuegos desea ingresar? "))
            if n > 0:
                return n
            else:
                print("Debe ingresar un número mayor a 0.")
        except ValueError:
            print("Error: ingrese un número válido.")
def get_game_data():
    nombre = input("Nombre: ")
    genero = input("Género: ")
    desarrollador = input("Desarrollador: ")
    clasificacion = input("Clasificación ESRB: ")
    return {
        "nombre": nombre,
        "genero": genero,
        "desarrollador": desarrollador,
        "clasificacion": clasificacion
    }
def write_csv_file(file_path, data, headers, delimiter):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, headers, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
        print("\nArchivo guardado correctamente ✅")
        print("Ruta completa:", os.path.abspath(file_path))
    except Exception as e:
        print("Error al guardar el archivo:", e)
def main():
    headers = ["nombre", "genero", "desarrollador", "clasificacion"]
    games = []
    n = ask_number()
    for i in range(n):
        print(f"\nVideojuego #{i+1}")
        game = get_game_data()
        games.append(game)
    write_csv_file("videojuegos_comas.csv", games, headers, delimiter=",")
    write_csv_file("videojuegos_tabs.csv", games, headers, delimiter="\t")
if __name__ == "__main__":
    main()
#############
