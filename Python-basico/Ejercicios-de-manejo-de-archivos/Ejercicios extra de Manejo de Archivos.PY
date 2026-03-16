def read_file_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]
def join_lines(lines):
    return " ".join(lines)
def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f'"{content}"')
def main():
    input_file = "input.txt"
    output_file = "output.txt"
    lines = read_file_lines(input_file)
    single_line_text = join_lines(lines)
    write_to_file(output_file, single_line_text)
    print("Process completed successfully.")
if __name__ == "__main__":
    main()
#######################
def read_file_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.readlines()
def convert_to_uppercase(lines):
    return [line.upper() for line in lines]
def write_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
def main():
    input_file = "input.txt"
    output_file = "output.txt"
    lines = read_file_lines(input_file)
    upper_lines = convert_to_uppercase(lines)
    write_file(output_file, upper_lines)
    print("File successfully converted to uppercase.")
if __name__ == "__main__":
    main()
######################
def get_user_input():
    return input("Enter a line of text: ")
def append_to_file(filename, text):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")
def main():
    filename = "registro.txt"
    user_text = get_user_input()
    append_to_file(filename, user_text)
    print("The text was successfully added to the file.")
if __name__ == "__main__":
    main()
