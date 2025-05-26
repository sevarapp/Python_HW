# Homework 1: Modify String with Underscores
def modify_string(txt):
    result = []
    i = 0
    count = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            # Check if underscore needs to be shifted
            if txt[i] in "aeiouAEIOU" or (i + 1 < len(txt) and txt[i + 1] == '_'):
                count -= 1  # Don't reset count, move underscore later
            else:
                if i + 1 < len(txt):
                    result.append('_')
                    count = 0
        i += 1
    return ''.join(result)

print("Homework 1 Examples:")
print(modify_string("hello"))          # hel_lo
print(modify_string("assalom"))        # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef
print()


# Homework 2: Integer Squares Exercise
def print_squares(n):
    for i in range(n):
        print(i * i)

print("Homework 2 Example:")
print_squares(5)
print()


# Homework 3: Loop-Based Exercises

# Exercise 1
print("Exercise 1:")
i = 1
while i <= 10:
    print(i)
    i += 1
print()

# Exercise 2
print("Exercise 2:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
print()

# Exercise 3
print("Exercise 3:")
num = 10
total = sum(range(1, num + 1))
print(f"Sum is: {total}")
print()

# Exercise 4
print("Exercise 4:")
n = 2
for i in range(1, 11):
    print(n * i)
print()

# Exercise 5
print("Exercise 5:")
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 < num < 200:
        print(num)
print()

# Exercise 6
print("Exercise 6:")
number = 75869
print("Output:", len(str(number)))
print()

# Exercise 7
print("Exercise 7:")
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
print()

# Exercise 8
print("Exercise 8:")
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
print()

# Exercise 9
print("Exercise 9:")
for i in range(-10, 0):
    print(i)
print()

# Exercise 10
print("Exercise 10:")
for i in range(5):
    print(i)
else:
    print("Done!")
print()

# Exercise 11
print("Exercise 11:")
print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
print()

# Exercise 12
print("Exercise 12:")
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end='  ')
    a, b = b, a + b
print("\n")

# Exercise 13
print("Exercise 13:")
from math import factorial
num = 5
print(f"{num}! = {factorial(num)}")
print()


# Homework 4: Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    from collections import Counter
    c1, c2 = Counter(list1), Counter(list2)
    result = []
    for item in (c1.keys() | c2.keys()):
        count = abs(c1[item] - c2[item])
        result.extend([item] * count)
    return result

print("Homework 4 Examples:")
print(uncommon_elements([1, 1, 2], [2, 3, 4]))         # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))         # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
