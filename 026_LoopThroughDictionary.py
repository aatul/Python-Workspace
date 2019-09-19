"""
Loop through Dictionary

You can use loop with dictionary to access keys, values and both as needed.
To access values from dictionary through loop, one can also use values().
"""

# define a dictionary
dict1 = {
    "language" : "Java",
    "author" : "James Gosling",
    "year" : "1995"
}

# print all key names
print("\nHere are all key names:")
for x in dict1:
    print(x)

# print all values
print("\nHere are all values:")
for x in dict1:
  print(dict1[x])

# print all values using values()
print("\nHere are all values using values():")
for x in dict1.values():
  print(x)

# print both keys and values using items()
print("\nHere are all keys and values:")
for x, y in dict1.items():
  print(x, y)