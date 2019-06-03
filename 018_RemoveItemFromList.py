"""
Remove Item
There are several methods to remove items from list1 list:
1. remove() - Removes specific item
2. pop() - removes the specified index, 
           (or the last item if index is not specified)
3. del keyword with given index number
4. del keyword to delete whole list
5. clear() - empties the list
"""

# define an list
list1 = ["Java","C","CPP","Android","HTML","Dart","Go"] 
list2 = ["Angular","React","Express","Flutter","Node"]

# using remove() method
list1.remove("C")
print(list1)

# using pop() method with index number
list1.pop(1)
print(list1)

# using pop() method without index number
list2.pop()
print(list2)

# using del() method item with index number
del list1[1]
print(list1)

# using del() method to delete whole list
del list2
# print(list2) - will throw an error since list2 deleted

# using clear() method
list1.clear()
print(list1)