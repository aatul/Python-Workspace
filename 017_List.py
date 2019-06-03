# define a list
list1 = ["Java","C","CPP","Android","HTML","Dart","Go"] 

print(list1) # print whole list

print(list1[1]) # prints 1st element

# print the number of items in list i.e. length
print(len(list1)) 

list1[2]="HTML" # replace element from given index no.
print(list1)

# printing list with for loop
for x in list1:
    print(x)

# check if item exists
if "Android" in list1:
  print("Yes, 'Android' is in the list")

# Add item or append an item in list
list1.append("Python")
print(list1)

# Insert an item as the given position
list1.insert(1, "R")
print(list1)

# reverse a list
list1.reverse()
print(list1)

# find index of item specified
x = list1.index("Python")
print(x)