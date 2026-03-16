def count_character(text, character):
    counter = 0

    for letter in text:
        if letter == character:
            counter += 1

    return counter
text = "programacion"
char = "o"
result = count_character(text, char)
print(f"Se ha encontrado {result} veces el carácter")
##################
def filter_words(words, n):
    filtered_list = []
    for word in words:
        if len(word) > n:
            filtered_list.append(word)
    return filtered_list
words_list = ["cielo", "sol", "maravilloso", "día"]
number = 4
result = filter_words(words_list, number)
print(result)
###############
def count_vowels(text):
    vowels = "aeiouAEIOU"
    counter = 0
    for letter in text:
        if letter in vowels:
            counter += 1
    return counter
result = count_vowels("Hola mundo")
print(result)
