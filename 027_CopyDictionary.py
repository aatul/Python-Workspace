"""
COPY DICTIONARY

You cannot copy a dictionary simply by typing dict2 = dict1, 
because: dict2 will only be a reference to dict1, 
and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, 
1. copy()
2. dict() constructor

dict() constructor can also be used to create new dictionary
"""

# define a dictionary
dict1 = {
    "language" : "Java",
    "author" : "James Gosling",
    "year" : "1995"
}

# using copy() to copy dictionary
dict2 = dict1.copy()
print("Copy Using copy()")
print(dict2)

# using dict() to copy dictionary
dict3 = dict(dict1)
print("Copy Using dict() constructor")
print(dict3)

# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
dict4 =	dict(language="Python", author="Guido van Rossum", year=1991)
print("Created new dictionary using dict() constructor")
print(dict4)