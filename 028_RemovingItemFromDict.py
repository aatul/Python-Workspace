"""
Remove Item
There are several methods to remove items from dictionary:
1. pop() - removes item with specified key name
2. popitem() - removes the last inserted item (in versions before 3.7, a random item is removed instead)
3. del keyword with given key name
4. del keyword to delete whole dictionary
5. clear() - empties the dictionary
"""

# define a dictionary
dict1 = {
    "language" : "Java",
    "author" : "James Gosling",
    "year" : "1995",
    "type" : "Object Oriented",
    "dificulty_level" : "Intermediate"
}

# print original dictionary
print("Original Dictionary")
print(dict1)

# using pop()
dict1.pop("author")
print("After pop()")
print(dict1)

# using popitem()
dict1.popitem()
print("After popitem()")
print(dict1)

# using del keyword, delete specific item with key specified
del dict1["type"]
print("After deleting specific item")
print(dict1)

# using clear()
dict1.clear()
print("After clear()")
print(dict1)

# using del keyword, delete whole dictionary
del dict1
print("Dictionary completely deleted")