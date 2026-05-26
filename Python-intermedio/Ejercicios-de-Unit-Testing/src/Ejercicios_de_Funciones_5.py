
def count_case_letters(text):
    upper_count = 0
    lower_count = 0
    for character in text:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
    return upper_count, lower_count
