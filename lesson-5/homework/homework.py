
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2024))




# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, n.

# Constraints

# 1 <= n <= 100

n=int(input("please give one number: "))
if n>1 and n<100:
    if n%2==1 :
        print("weird")
    elif n%2==0 and n>=2 and n<=5 :
        print("not weird")
    elif n%2==0 and n>=6 and n<=20 :
        print("weird")
    elif n%2==0 and n>20 :
        print("not weird")
else:
    print('out of range')



a = 3
b = 10

# Check if we need to count down or up
if a > b:
    # If a is greater and even, start from a; if odd, go to previous even number
    start = a if a % 2 == 0 else a - 1
    # Generate even numbers in reverse order (decreasing by 2)
    result = list(range(start, b - 1, -2))
else:
    # If a is smaller and even, start from a; if odd, go to next even number
    start = a if a % 2 == 0 else a + 1
    # Generate even numbers in increasing order (step of 2)
    result = list(range(start, b + 1, 2))

print(result)  # Print the list of even numbers


a = 3
b = 10

# Make sure low is the smaller number and high is the bigger one
low, high = sorted([a, b])

# If low is odd, low % 2 = 1 → add 1 to get the next even number
# If low is even, low % 2 = 0 → start remains the same
start = low + (low % 2)

# Generate even numbers from start to high (inclusive) with step 2
result = list(range(start, high + 1, 2))

# If original a was bigger than b, reverse the result
if a > b:
    result = result[::-1]

print(result)  # Print the list of even numbers

