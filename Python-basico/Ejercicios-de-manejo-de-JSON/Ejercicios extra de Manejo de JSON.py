import json
def load_pokemon():
    with open("pokemon.json", "r", encoding="utf-8") as file:
        return json.load(file)
def show_basic_info(pokemon_list):
    print("\nPokémon list:\n")
    for pokemon in pokemon_list:
        for key, value in pokemon.items():
            print(key + ":", value)
        print("-------------------")
def search_by_type(pokemon_list):
    search_type = input("Enter the Pokémon type you want to search for: ").strip().lower()
    print("\nThe Pokémon of that type are:\n")
    found = False
    for pokemon in pokemon_list:
        if pokemon["type"].lower() == search_type:
            print(pokemon["name"])
            found = True
    if not found:
        print("No Pokémon found for that type.")
def show_stats(pokemon_list):
    print("\nPokémon stats:\n")
    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        print(f"Attack: {pokemon['attack']}")
        print(f"Defense: {pokemon['defense']}")
        print(f"Speed: {pokemon['speed']}")
        print("-------------------")
def show_average_level_by_type(pokemon_list):
    type_levels = {}
    for pokemon in pokemon_list:
        pokemon_type = pokemon["type"]
        level = pokemon["level"]
        if pokemon_type not in type_levels:
            type_levels[pokemon_type] = []
        type_levels[pokemon_type].append(level)
    print("\nAverage level by type:\n")
    for pokemon_type, levels in type_levels.items():
        average_level = sum(levels) / len(levels)
        print(f"Type: {pokemon_type} -> Average level: {average_level:.1f}")
def main():
    pokemon_list = load_pokemon()
    print("1. Show name, type, and level")
    print("2. Search Pokémon by type")
    print("3. Show Pokémon stats")
    print("4. Show average level by type")
    option = input("\nChoose an option: ")
    if option == "1":
        show_basic_info(pokemon_list)
    elif option == "2":
        search_by_type(pokemon_list)
    elif option == "3":
        show_stats(pokemon_list)
    elif option == "4":
        show_average_level_by_type(pokemon_list)
    else:
        print("Invalid option.")
if __name__ == "__main__":
    main()
