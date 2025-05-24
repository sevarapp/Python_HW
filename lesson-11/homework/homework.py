
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b



def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# ----------------------------------------
# Package: geometry.circle (Simulated)
# ----------------------------------------

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius


 ----------------------------------------

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{file_path}' not found."

# ----------------------------------------
# Package: file_operations.file_writer (Simulated)
# ----------------------------------------

def write_file(file_path, content):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"✅ Content successfully written to {file_path}")
    except Exception as e:
        print(f"❌ Failed to write to file: {e}")


