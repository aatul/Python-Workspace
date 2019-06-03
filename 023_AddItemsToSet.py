"""
Adding Items to SET

There are two methods with set, which can ne used to add item(s) to set.
1. add()    - Adds single item to Set
2. update() - Adds more than one or multiple items to Set
"""

# define a set
set1 = {"Java","C","CPP"}
print(set1)

# using add()
set1.add("Android")
print(set1)

# using update()
set1.update(["HTML","Dart","Go"])
print(set1)