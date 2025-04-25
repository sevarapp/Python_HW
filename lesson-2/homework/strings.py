1. Age Calculator

# Import datetime module to get the current year
from datetime import datetime

# Ask user for their name
name = input("Enter your name: ")

try:
    # Ask user for year of birth and convert to integer
    birth_year = int(input("Enter your year of birth: "))
    # Get the current year
    current_year = datetime.now().year
    # Calculate age
    age = current_year - birth_year
    # Display the result
    print(f"\nHello {name}, you are {age} years old.")
except ValueError:
    # Handle invalid input
    print("\nPlease enter a valid year.")

 2. Extract Car Names (1)

# Given string
txt = 'LMaasleitbtui'
# Extract characters at even indices (every 2nd character)
car_name = txt[::2]
# Display the result
print(f"\nExtracted car name: {car_name}")
```

---

3. Extract Car Names (2)

# Given string
txt = 'MsaatmiazD'
# Extract characters at even indices (every 2nd character)
car_name = txt[::2]
# Display the result
print(f"\nExtracted car name: {car_name}")



4. Extract Residence Area

# Given sentence
txt = "I'am John. I am from London"

# Check if "from" is in the sentence
if "from" in txt:
    # Get the part after "from"
    area = txt.split("from")[-1].strip()
    # Display the area
    print(f"\nResidence area: {area}")
else:
    # Message if "from" is not found
    print("\nResidence area not found.")


---

5. Reverse String

# Ask user for a string
user_input = input("Enter a string to reverse: ")
# Reverse the string using slicing
reversed_str = user_input[::-1]
# Display the reversed string
print(f"\nReversed string: {reversed_str}")


---

6. Count Vowels

# Ask user for a string
user_input = input("Enter a string: ")
# List of vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"
# Count how many characters in the string are vowels
count = sum(1 for char in user_input if char in vowels)
# Display the count
print(f"\nNumber of vowels: {count}")


---

7. Find Maximum Value
python
try:
    # Ask user to input numbers separated by space
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    # Find the maximum number in the list
    max_val = max(numbers)
    # Display the result
    print(f"\nMaximum value: {max_val}")
except ValueError:
    # Handle invalid input
    print("\nPlease enter only numbers.")


---

 8. Check Palindrome

# Ask user for a word
word = input("Enter a word: ")
# Check if the word reads the same forwards and backwards
if word == word[::-1]:
    print(f"\n'{word}' is a palindrome.")
else:
    print(f"\n'{word}' is not a palindrome.")


9. Extract Email Domain

# Ask user for an email address
email = input("Enter your email address: ")
# Check if the email contains "@"
if "@" in email:
    # Get the domain part of the email
    domain = email.split("@")[1]
    # Display the domain
    print(f"\nEmail domain: {domain}")
else:
    # Message for invalid email
    print("\nInvalid email address.")


---

 10. Generate Random Password

# Import required modules
import random
import string

# Set the password length
length = 12
# Combine all possible characters
characters = string.ascii_letters + string.digits + string.punctuation
# Randomly choose characters to form the password
password = ''.join(random.choice(characters) for _ in range(length))
# Display the password
print(f"\nGenerated password: {password}")



