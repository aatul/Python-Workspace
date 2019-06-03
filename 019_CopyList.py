"""
Copy List
You cannot copy list1 list simply by typing list2 = list1, 
because: list2 will only be list1 reference to list1, 
and changes made in list1 will automatically also be made 
in list2.

There are ways to make list copy, List methods:
1. copy()
2. list()
"""

list3 = ["MySQL","Oracle","SQLite","Mongo"]

# using copy() method
list4 = list3.copy()
print(list4)

# using list() method
list5 = list(list3)
print(list5)