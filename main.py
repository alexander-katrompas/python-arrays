"""
Arrays and array-like structures are fundamental to programming and computer
science. Most of the programming you will do will work with array-like
structures so it is critical to understand them and the differences between
them. This set of examples will walk you through the different array-like
structures in Python, but all languages have similar concepts. The most
important thing to note is that all array-like structures basically work
the same. It's all about the index or key that you use to access the structure.
Once you understand the index or key structure and how the hierarchy of indexes
and keys work, then all array-like structures work the same.
"""

# bring numpy arrays into Python (they are not part of Python natively)
import numpy as np

# for use in the examples to make random numbers
import random

# constants to control the examples. you can change these to whatever you
# like and the examples still work. make sure you understand this and why.
SIZE = 5
ROWS = 3
COLS = 4

######################################
# NUMPY ARRAY EXAMPLES
######################################

# this creates a numpy array. it has the characteristics that
# it is a fixed size of SIZE and fixed type, in this case ints.
numbers = np.array([0] * SIZE, dtype=int)

# put the number 6 in the second position
numbers[1] = 6

# read the number from the second position
print(numbers[1])

# put the number 10 in all positions
for i in range(SIZE):
    numbers[i] = 10

# print all the numbers in the array, one per line, along with the index
for i in range(SIZE):
    print(i, ":", numbers[i])

# OR just dump out the whole array all at once.
print(numbers)
print()

######################################
# PYTHON LIST EXAMPLE
######################################

"""
A python list is an array-like structure. Technically it is not an array.
It is an object with array-like properties and you use it like an array,
and you can do many other things with it. The basics of array usage still apply.
"""

# Python lists are variable size and variable type
# contrast that with numpy arrays which are fixed/fixed.

# this makes an list with three elements of differnt types; int, string, float
python_list = [10, "cat", 3.14]

# print all the values in the list, one per line, along with the index
s = len(python_list) # first get the size of the list
for i in range(s):
    print(i, ":", python_list[i])

# you can add items to the list dynamically
python_list.append("dog")

#print the last item in the list
print(python_list[-1])

# you can dump out the whole list all at once.
print(python_list)
print()

######################################
# PYTHON TUPLE EXAMPLES
######################################
"""
A Python Tuple is an array like structure that is exactly the same as a list
except you cannot dynamically alter the size. So a tuple is a list that is
fixed size with variable types.
"""

# make a tuple of various types
python_tuple = (100, "hello", 3.14, "world")

# print all the values in the tuple, one per line, along with the index
s = len(python_tuple) # first get the size of the tuple
for i in range(s):
    print(i, ":", python_tuple[i])

# OR just dump out the whole tuple all at once.
print(python_tuple)
print()

######################################
# PYTHON DICTIONARY EXAMPLES
######################################
"""
A Python Dictionary is an array like structure that is exactly the same as a
list except the indexes are not numbers, they are keys (a string).
So a dictionary is a list that is variable size with variable types and has
a key instead of an index.
"""

# create a dictionary of key:value pairs
python_dictionary = {"one": 50, "pi": 3.14, "helloworld": "this is a longer string"}

for key in python_dictionary:
    print(key, ":", python_dictionary[key])

# OR just dump out the whole tuple all at once.
print(python_dictionary)

# you can add items to the dictionary dynamically
# just make a new key with a new value
python_dictionary["dog"] = "cat"

#print the item just added
print(python_dictionary["dog"])

# you can dump out the whole list all at once.
print(python_dictionary)
print()

######################################
# Array-like structures inside array-like structures.
# i.e. multidimensional arrays.
######################################

"""
You can place any array like structure inside another array like structure.
This creates what is known as a multimentional array.
"""
# create a ROWS x COLS array
num2d = np.zeros((ROWS, COLS), dtype=int)

# show the array
print(num2d)

# fill the array with numbers
# 1,1,1,1
# 2,2,2,2
# 3,3,3,3
for i in range(ROWS):
    for j in range(COLS):
        num2d[i][j] = i+1
        
# show the array
print(num2d)

# print each row one at at a time
for i in range(ROWS):
    print(num2d[i])
    
# print each element one at a time
for i in range(ROWS):
    for j in range(COLS):
        print(num2d[i][j], end=" ")
    print()
print()


# it is VERY common to make n-dimension "arrays" with dictionaries
# the following is a 2D dictionary where the "rows" are accessed by each key
# and the "columns" are each piece of data in the lists in the dictionary.
# i.e. this is a 1D dictionary that holds multiple 1D lists

# make a dictionary that holds three people's names as keys
# and has their age, gender, and favorite color as each value
people = {"alice": [29, "f", "red"], "bob": [24, "m", "green"], "charlie": [32, "m", "blue"]}

# show the dictionary
print(people)

# add 1 to everyone's age
for name in people:
    # this goes to the 1st element in the list accessed by the name
    people[name][0] += 1

# show the dictionary
print(people)

# flip everyone's gender
for name in people:
    if people[name][1] == 'm':
        people[name][1] = 'f'
    else:
        people[name][1] = 'm'
        
# show the dictionary
print(people)

# capitalize all the colors
for name in people:
    people[name][2] = people[name][2].upper()
        
# show the dictionary
print(people)

# change bob's color to purple
people['bob'][2] = 'purple'

# show the dictionary
print(people)
print()

######################################
# Strings
######################################

"""
Strings are also an array-like structure in all languages.
In Python they are tuples with a fixed type; characters.
i.e. A string in Python is a fixed size fixed type list
that contains only character types.
"""

# make a string
mystring = "hello world"

# print each character one at a time
for ch in mystring:
    print(ch, end="")
print()

# print each character one at a time using indexes
l = len(mystring)
for i in range(l):
    print(mystring[i], end="")
print()

# capitalize every other letter into a new string
new_string = ""
for i in range(l):
    if i%2:
        new_string += mystring[i].upper()
    else:
        new_string += mystring[i]

print(new_string)

# print the string backwards
for i in range(l-1, -1, -1):
    print(mystring[i], end="")
print()
print()

########################################################
# FINDING TOTAL, AVERAGE, MIN, MAX
########################################################

"""
Finding the min and max, and getting totals and averages are a common things
to do in array-like structures. While Python provide many "magic" methods
to do this, it is VERY imporatant to learn to do this manually. The following
will demonstrate how this can be done manually.
"""

# create an 'empty' numpy array of size SIZE
rnums = np.empty(SIZE, dtype="int")

# fill the array with randome integers from 1 to 10 (inclusive)
for i in range(SIZE):
    rnums[i] = random.randint(1,10)

#show the array
print(rnums)

# get the total
total = 0
for i in range(SIZE):
    total += rnums[i]
print("total:", total)

# get the average
average = float(total)/float(SIZE)
# print it to two decimal places
print("average: {:.{prec}f}".format(average, prec=2))

# get the min
min = rnums[0] # priming read to get a start value
for i in range(1, SIZE):
    if rnums[i] < min: min = rnums[i]
print("min:", min)

# get the max
max = rnums[0] # priming read to get a start value
for i in range(1, SIZE):
    if rnums[i] > max: max = rnums[i]
print("max:", max)
print()

########################################################
# USING FUNCTIONS WITH FLAGS
########################################################

"""
Note in the above example the code to find the min and max is VERY similar.
When that happens, you should not write two versions of the same code. You
should write it once, and use it multiple times. In this case, the only
differnence is the less-than and greater-than signs. We can make this into
a single min_max function that is controlled by a flag to determine which
operation to perform.
"""

def min_max(arr, mini):
    # arr is an array
    # min is a boolean to control the output
    l = len(arr)
    minmax = arr[0] # priming read to get a start value
    for i in range(1, l):
        if(mini):
            if arr[i] < minmax: minmax = arr[i]
        else:
            if arr[i] > minmax: minmax = arr[i]
    return minmax
    
print("min:", min_max(rnums, True))    
print("max:", min_max(rnums, False))
print()

########################################################
# USING FUNCTIONS WITH FLAGS WITH DEFAULT VALUES
########################################################

"""
In the function above, we can make a small change so that the minimum is
assumed, and then we can override it to the max if we choose. This is
done with a default value for min.
"""
def min_max2(arr, mini=True):
    # arr is an array
    # min is a boolean to control the output
    l = len(arr)
    minmax = arr[0] # priming read to get a start value
    for i in range(1, l):
        if(mini):
            if arr[i] < minmax: minmax = arr[i]
        else:
            if arr[i] > minmax: minmax = arr[i]
    return minmax
    
# now when we call min_max2, we only need to pass a boolean
# to the flag if want to change the default value
print("min:", min_max2(rnums))
print("max:", min_max2(rnums, False))
print()

########################################################
# PROFESSIONAL CODING
########################################################
"""
In the fucntions above there is no error checking for passed in values.
This would not be acceptable in ANY professional code. It is ALWAYS
your responsibility to check for errors in data and data types.
This demonstrates a complete, professional version of the min_max function.
This will also demonstrate the correct usage of the Try/Except statement.
"""

def minmaxpro(arr, mini=True):
    # we need a default value to return if needed
    # it is not needed here, but this is best practice
    minmax = None 

    if type(arr) != type(np.empty(0, dtype="int")):
        raise TypeError('array must be a Numpy integer array')
    elif type(mini) != bool:
        raise TypeError('parameter min must be Boolean')
    else:
        l = len(arr)
        minmax = arr[0] # priming read to get a start value
        if(mini):
            for i in range(1, l):
                if arr[i] < minmax: minmax = arr[i]
        else:
            for i in range(1, l):
                if arr[i] > minmax: minmax = arr[i]
    return minmax
    

# using the minmaxpro function correctly
try:
    print("min:", minmaxpro(rnums))
except TypeError as e:
    print(e)

try:
    print("max:", minmaxpro(rnums, False))
except TypeError as e:
    print(e)

# now try it with a non-numpy array
a = [10,20,30] # this is a Python List, not a Numpy array
try:
    print("min:", minmaxpro(a))
except TypeError as e:
    print(e)

# now try it with a float instead of a boolean for min
n = 1.234
try:
    print("min:", minmaxpro(rnums, n)) # n is a float, not a boolen
except TypeError as e:
    print(e)

print()
