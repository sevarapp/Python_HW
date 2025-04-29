# # Homework: List and Tuple Exercises

# ## 1. Create and Access List Elements
# #Create a list containing five different fruits and print the third fruit.
fruitss=['cherry','banana','pineapple','mango','apple']
print (fruitss[2])

# ## 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
odd_numbers=[1,3,5,5,5,7,9]
even_numbers=[2,2,2,4,6,8,10]
new=odd_numbers+even_numbers
print(new)

# ## 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
new_list=[1,3,4,55,9,99,100,109]
n_list=[]
n_list.append(new_list[0])
n_list.append(new_list[len(new_list)//2]) #finding length and dividing by 2
n_list.append(new_list[len(new_list)-1]) #accessing the last element by len function
print(n_list)


# ## 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
fav_movies=['comedy','horror','action','romance','documentary']
fav_movies_tuple=tuple(fav_movies)
print(fav_movies_tuple)


# ## 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities=['Tashkent','Moscow','Paris','London','Columbia']
if 'Paris' in cities:
    print('exists')
else:
    print('not in the list')

# ## 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.

d1=['hey', 'john','bye']
d2=d1.copy()
print(d2)

# ## 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
number_list = [10, 20, 30, 40, 50]
number_list[0], number_list[-1] = number_list[-1], number_list[0]
print("Swapped list:", number_list)



# ## 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

tuple_88 = tuple(range(1, 11))
slice_result = tuple_88[3:8]
print("Sliced tuple (from index 3 to 7): ", slice_result)


# ## 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ["blue", "red", "green", "blue", 'blue', "yellow", "blue"]
count_blue = colors.count("blue")
print("'blue' appears:", count_blue,'times')

# ## 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".

animals = ("bear", "lion", "wolf", "tiger", "fox")
lion_index = animals.index("lion")
print("Index of 'lion':", lion_index)

# ## 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.

tupple=(18,18,19,20,21,17)
tupplee=(40,43,45,50,51)
merged_one=tupple+tupplee
print(merged_one)

# ## 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
t2uple=('Hey',"i",'am','sevara')
l2ist=['how','are','you']
lent=len(t2uple)
lenl=len(l2ist)
print (lent)
print(lenl)

# ## 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
tuple5=(34,45,65,55,12)
list_tuple=list(tuple5)
print(list_tuple)


# ## 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.

num_tuple = (41, 49, 51, 43, 47, 46)
max_val = max(num_tuple)
min_val = min(num_tuple)
print("Max is :", max_val)
print("Min is :", min_val)



# ## 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
my_tuple=(2,4,8,1,'hey')
new_reversed=my_tuple[::-1]
print(new_reversed) 
