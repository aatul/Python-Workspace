"""
Set
Set is one more type of collection such as List and Tuple.
The difference is Set is written with curly brackets.
And it is unordered, unchangeable and unindexed similar to Tuple.
That means once set is created you cannot change the values.
This also means once set is created you cannot change items but you can add items to it.
And you can remove items from set similar to List unlike Tuple.
But we can also delete set.
"""

# define a set
set1 = {"Java","C","CPP","Android","HTML","Dart","Go"}

# print the number of items in set i.e. length
print("Lenght of Set: "+str(len(set1)))

# loop with set
for x in set1:
    print(x)

# check if item exists
if "Android" in set1:
    print("Yes, 'Android' is in the Set")

# set constuctor, can be used to create set
set2 = set(("Angular","React","Express","Flutter","Node"))
# note the double round-brackets, used to define contructor
print(set2)