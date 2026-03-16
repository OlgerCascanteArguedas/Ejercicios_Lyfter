import csv
def read_and_display(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print("\nNombre:", row[0])
                print("Género:", row[1])
                print("Desarrollador:", row[2])
                print("Clasificación:", row[3])
                print("-" * 30)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print("Ocurrió un error:", e)
def filter_by_esrb(file_path):
    try:
        esrb = input("Ingrese la clasificación ESRB (E, T, M, etc): ").strip().upper()
        found = False
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["clasificacion"].strip().upper() == esrb:
                    print(f"\nNombre: {row['nombre']}")
                    print(f"Género: {row['genero']}")
                    print(f"Desarrollador: {row['desarrollador']}")
                    print(f"Clasificación: {row['clasificacion']}")
                    print("-" * 30)
                    found = True

        if not found:
            print("No se encontraron videojuegos con esa clasificación.")

    except FileNotFoundError:
        print("Error: el archivo no existe o la ruta es incorrecta.")
    except Exception as e:
        print("Ocurrió un error:", e)
def count_by_genre(file_path):
    try:
        genre_count = {}

        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                genre = row["genero"].strip()

                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1

        if not genre_count:
            print("No hay datos en el archivo.")
            return
        print("\nGéneros encontrados:")
        for genre in sorted(genre_count):
            print(f"{genre}: {genre_count[genre]}")
    except FileNotFoundError:
        print("Error: el archivo no fue encontrado.")
    except KeyError:
        print("Error: la columna 'genero' no existe en el archivo.")
    except Exception as e:
        print("Ocurrió un error:", e)
def search_by_developer(file_path):
    try:
        developer_input = input("Ingrese el nombre del desarrollador: ").strip().lower()
        found_games = []
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                developer = row["desarrollador"].strip().lower()
                if developer == developer_input:
                    found_games.append(row)
        if found_games:
            print(f"\nVideojuegos desarrollados por {developer_input.title()}:")
            for game in found_games:
                print(f"- {game['nombre']} "
                      f"(Clasificación: {game['clasificacion']}, "
                      f"Género: {game['genero']})")
        else:
            print("No se encontraron videojuegos para ese desarrollador.")

    except FileNotFoundError:
        print("Error: el archivo no fue encontrado.")
    except KeyError:
        print("Error: el archivo no tiene la columna esperada.")
    except Exception as e:
        print("Ocurrió un error:", e)
def main():
    read_and_display("videojuegos.csv")
    filter_by_esrb("videojuegos.csv")
    count_by_genre("videojuegos.csv")
    search_by_developer("videojuegos.csv")
if __name__ == "__main__":
    main()
