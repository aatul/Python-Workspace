"""
Removing Items from SET

There are several methods to remove items from set1 :
1. remove() - Removes specific item
2. discard() - Removes specific item
2. pop() - Removes an item, but this method will remove the last item. Remember that sets are unordered, so we cannot predict which item will be removed.
4. del keyword - to delete whole set
5. clear() - empties the set
"""

# define a set
set1 = {"Java","C","CPP","Android","HTML","Dart","Go"}
print("Original Set: "+str(set1))

# using remove() method
set1.remove("C")
print("Set 1 after removing 'C': "+str(set1))

# using discard() method
set1.discard("CPP")
print("Set 1 after discarding 'CPP': "+str(set1))

# using pop()
removedItem = set1.pop()
print("Popped item: "+removedItem) # print popped item
print("Set 1 after pop: "+str(set1))

# using clear()
set1.clear()
print("Set 1 after clear: "+str(set1))

del set1
# print(set1) - will throw an error since set1 deleted
print("Set1 deleted.")
