import os
import random
import string

# Exception Handling Exercises

def divide_by_zero():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError handled: {e}")

def validate_integer_input():
    try:
        num = int(input("Enter an integer: "))
    except ValueError as e:
        print(f"ValueError handled: {e}")

def open_missing_file():
    try:
        with open('nonexistent.txt', 'r') as f:
            f.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError handled: {e}")

def type_checking():
    try:
        a = input("Enter first number: ")
        b = input("Enter second number: ")
        result = float(a) + float(b)
        print(f"Result: {result}")
    except ValueError:
        raise TypeError("Inputs must be numerical.")

def permission_error_handler():
    try:
        with open('/root/secure.txt', 'r') as f:
            f.read()
    except PermissionError as e:
        print(f"PermissionError handled: {e}")

def list_index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError handled: {e}")

def handle_keyboard_interrupt():
    try:
        input("Enter a number (Ctrl+C to cancel): ")
    except KeyboardInterrupt:
        print("KeyboardInterrupt handled: User canceled input")

def arithmetic_error():
    try:
        result = 1 / 0
    except ArithmeticError as e:
        print(f"ArithmeticError handled: {e}")

def unicode_decode_error():
    try:
        with open('example.txt', 'rb') as f:
            content = f.read().decode('utf-16')
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError handled: {e}")

def attribute_error_example():
    try:
        x = 5
        x.append(3)
    except AttributeError as e:
        print(f"AttributeError handled: {e}")

# File Input/Output Exercises

def read_entire_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def read_first_n_lines(filepath, n):
    with open(filepath, 'r') as file:
        return [next(file) for _ in range(n)]

def append_and_display(filepath, text):
    with open(filepath, 'a') as file:
        file.write(text + '\n')
    return read_entire_file(filepath)

def read_last_n_lines(filepath, n):
    with open(filepath, 'r') as file:
        return file.readlines()[-n:]

def read_lines_to_list(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

def read_lines_to_variable(filepath):
    with open(filepath, 'r') as file:
        return ''.join(file.readlines())

def read_lines_to_array(filepath):
    return read_lines_to_list(filepath)

def find_longest_words(filepath):
    with open(filepath, 'r') as file:
        words = file.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]

def count_lines(filepath):
    with open(filepath, 'r') as file:
        return sum(1 for _ in file)

def count_word_frequency(filepath):
    from collections import Counter
    with open(filepath, 'r') as file:
        words = file.read().replace(',', ' ').split()
        return Counter(words)

def get_file_size(filepath):
    return os.path.getsize(filepath)

def write_list_to_file(filepath, data):
    with open(filepath, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dst:
        dst.write(src.read())

def combine_files_line_by_line(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + line2)

def read_random_line(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        return random.choice(lines)

def check_file_closed(filepath):
    file = open(filepath, 'r')
    status = file.closed
    file.close()
    return status, file.closed

def remove_newlines(filepath):
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read().replace(',', ' ')
        return len(text.split())

def extract_characters_from_files(file_list):
    characters = []
    for file in file_list:
        with open(file, 'r') as f:
            characters.extend(list(f.read()))
    return characters

def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as f:
            f.write(f"This is file {letter}\n")

def create_alphabet_lines_file(filepath, letters_per_line=5):
    with open(filepath, 'w') as f:
        for i in range(0, 26, letters_per_line):
            f.write(' '.join(string.ascii_uppercase[i:i+letters_per_line]) + '\n')
