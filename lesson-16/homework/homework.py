import numpy as np

# 1. Convert List to 1D Array
print("Task 1: Convert List to 1D Array")
l1 = [12.23, 13.32, 100, 36.32]
array1d = np.array(l1)
print("Original List:", l1)
print("One-dimensional NumPy array:", array1d, "\n")

# 2. Create 3x3 Matrix (2–10)
print("Task 2: Create 3x3 Matrix from 2 to 10")
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print(matrix_3x3, "\n")

# 3. Null Vector (10) & Update Sixth Value
print("Task 3: Null Vector and Update Sixth Value to 11")
null_vector = np.zeros(10)
null_vector[6] = 11
print(null_vector, "\n")

# 4. Array from 12 to 38
print("Task 4: Array with values from 12 to 38")
array_12_38 = np.arange(12, 38)
print(array_12_38, "\n")

# 5. Convert Array to Float Type
print("Task 5: Convert Array to Float Type")
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("Original array:", int_array)
print("Float array:", float_array, "\n")

# 6. Celsius to Fahrenheit Conversion
print("Task 6: Celsius to Fahrenheit Conversion")
celsius = np.array([0, 12, 45.21, 34, 99.91, 0])
fahrenheit = celsius * 9 / 5 + 32
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit, "\n")

# 7. Append Values to Array
print("Task 7: Append Values to Array")
original_arr = np.array([10, 20, 30])
values_to_append = np.arange(40, 100, 10)
appended_array = np.append(original_arr, values_to_append)
print("Original array:", original_arr)
print("After append:", appended_array, "\n")

# 8. Array Statistical Functions
print("Task 8: Statistical Functions")
rand_array = np.random.rand(10)
print("Random array:", rand_array)
print("Mean:", np.mean(rand_array))
print("Median:", np.median(rand_array))
print("Standard Deviation:", np.std(rand_array), "\n")

# 9. Find Min and Max in 10x10 Array
print("Task 9: Find Min and Max in 10x10 Array")
array_10x10 = np.random.randint(0, 100, (10, 10))
print(array_10x10)
print("Minimum value:", array_10x10.min())
print("Maximum value:", array_10x10.max(), "\n")

# 10. Create 3x3 Identity Matrix
print("Task 10: Create 3x3 Identity Matrix")
identity_matrix = np.eye(3)
print(identity_matrix)
