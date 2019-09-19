"""
FOR LOOP

For loop is used to iterate over collections (such as list, tuple, set, dictionary) or strings.
It is very much similar to other programming language.
"""

# define a list
list1 = ["1","2","3","4"]
list2 = ["A","B","C","D"]

# print each item from list
print("Loop through list")
for x in list1:
  print(x)

# print each charater from string
print("\nLoop through string")
for x in "STRING":
  print(x)

# using 'break' keyword to stop loop
print("\nusing 'break' keyword")
for x in list1:
  print(x) 
  if x == "3":
    break

# using 'continue' keyword to stop current iteration and continue with next
print("\nusing 'continue' keyword")
for x in list1:
  if x == "3":
    continue
  print(x)

# nested for loop
print("\nNested For Loop")
for x in list1:
  for y in list2:
    print(x, y)