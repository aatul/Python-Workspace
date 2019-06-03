"""
Tuple
Tuple is another type of collection such as List.
The difference is tuple is written with round brackets.
And it is ordered and unchangeble.
That means once tuple is created you cannot change the values.
This also means once tuple is created you cannot add items to it.
And you cannot remove items from tuple.
But we can delete tuple.
"""

# define a tuple
tuple1 = ("Java","C","CPP","Android","HTML","Dart","Go")

# access tuple items using index number
print(tuple1[3])

# print the number of items in tuple i.e. length
print(len(tuple1))

# loop with tuple
for x in tuple1:
  print(x)

# check if item exists
if "Android" in tuple1:
  print("Yes, 'Android' is in the Tuple")

del tuple1
# print(tuple1) - will throw an error since tuple1 deleted

# tuple constuctor, can be used to create tuple
tuple2 = tuple(("Angular","React","Node","Express","Flutter","Node"))
# note the double round-brackets, used to define contructor
print(tuple2)

# returns the number of times a specified value occurs in a tuple
print(tuple2.count("Node"))

# returns the position/index of element where it was found
print(tuple2.index("Flutter"))