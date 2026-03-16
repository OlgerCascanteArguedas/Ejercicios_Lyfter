import json
import os
FILE_NAME = "pokemon.json"
def load_pokemon_file(file_name):
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                print("Warning: JSON file does not contain a list. Starting with an empty list.")
                return []
    except json.JSONDecodeError:
        print("Warning: The JSON file is empty or invalid. Starting with an empty list.")
        return []
def get_new_pokemon():
    name = input("Enter Pokémon name: ").strip()
    pokemon_type = input("Enter Pokémon type: ").strip()
    level = int(input("Enter Pokémon level: "))
    hp = int(input("Enter Pokémon HP: "))
    new_pokemon = {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "hp": hp
    }
    return new_pokemon
def save_pokemon_file(file_name, pokemon_list):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, indent=4, ensure_ascii=False)
def main():
    pokemon_list = load_pokemon_file(FILE_NAME)
    print("Current Pokémon in file:")
    for pokemon in pokemon_list:
        print(f"- {pokemon['name']}")
    new_pokemon = get_new_pokemon()
    pokemon_list.append(new_pokemon)
    save_pokemon_file(FILE_NAME, pokemon_list)
    print("\nNew Pokémon added successfully!")
    print(f"File saved at: {os.path.abspath(FILE_NAME)}")
if __name__ == "__main__":
    main()
