"""
DICTIONARY

A dictionary is a collection similar to List, Tuple and Set.
Dictionary is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
"""

# define a dictionary
dict1 = {
    "language" : "Java",
    "author" : "James Gosling",
    "year" : "1995"
}

# print the number of items in dictionary i.e. dictionary length
print(len(dict1))

# access dictionary
str1 = dict1["language"]
print(str1)

# access dict1 using get(); this will give same result
str2 = dict1.get("language")
print(str2)

# change value of a key
dict1["year"] = "1992"
print(dict1["year"])

# check if key exists
if "language" in dict1:
    print("Yes, 'language' is in the Dictionary")

# adding item to dictionary
dict1["type"] = "Object Oriented"
print(dict1)