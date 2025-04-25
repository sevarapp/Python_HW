import math

# 1. Square: Perimeter and Area
side = float(input("Enter the side of the square: "))
s_perimeter = 4 * side
s_area = side ** 2
print(f"Perimeter: {s_perimeter}, Area: {s_area}")

# 2. Circle: Length 
diam = float(input("Enter the diameter of the circle: "))
c_length = math.pi * diam
print(f" Circumference: {c_length}")

# 3. Mean of two numbers
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
mean = (a + b) / 2
print(f"Mean of {a} and {b} is {mean}")

# 4. Sum, Product, and Squares
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Sum: {sum_ab}, Product: {product_ab}, a²: {square_a}, b²: {square_b}")

