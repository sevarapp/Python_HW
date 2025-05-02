# Homework 4:Python Dictionary and Set Exercises
# Dictionary Exercises

# 1. Sort a Dictionary by Value
#  a Python script to sort (ascending and descending) a dictionary by value.
my_dict={'name':'Sevara','last_name':'Pulatova','age':'18'}
print(sorted(my_dict))


# 2. Add a Key to a Dictionary
#  a Python script to add a key to a dictionary.
my_dict['location']='UZB'
print(my_dict)

# ### 3. Concatenate Multiple Dictionaries
# a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
 
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# ### 4. Generate a Dictionary with Squares
# a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form `(x, x*x)`.
n = 19  # any positive integer
square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x

print(square_dict)

# ### 5. Dictionary of Squares (1 to 15)
# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
n = 15  # as it is stated in given problem
square_dict = {}
for x in range(1, n + 1):
    square_dict[x] = x * x
print(square_dict)


# ## Set Exercises
# ### 1. Create a Set
#a Python program to create a set.
my_set=set()

# ### 2. Iterate Over a Set
# a Python program to iterate over sets.

my_set={ 4,5,6,6,1,1}
for item in my_set:
    print (item)

# ### 3. Add Member(s) to a Set
# a Python program to add member(s) to a set.
my_set.update([('Kamila','Sevinch')])
print(my_set)

# ### 4. Remove Item(s) from a Set
# a Python program to remove item(s) from a given set.
my_set.discard(4)
print(my_set)


# ### 5. Remove an Item if Present in the Set
#a Python program to remove an item from a set if it is present in the set.
x=6
if x in my_set:
   my_set.discard(x)
   print(my_set)

else:
   print('not found')

