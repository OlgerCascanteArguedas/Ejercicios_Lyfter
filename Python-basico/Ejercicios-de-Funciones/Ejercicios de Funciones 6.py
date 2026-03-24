
################
def sort_hyphen_words(text):
    words = text.split("-")
    words.sort()
    sorted_text = "-".join(words)
    return sorted_text
result = sort_hyphen_words("python-variable-funcion-computadora-monitor")
print(result)
