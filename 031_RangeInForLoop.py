"""
The range() function:
    1. returns a sequence of numbers, starting from 0 by default
    2. increments by 1 (by default)
    3. ends at a specified number.
"""

# loop upto 5
for x in range(5):
  print(x)

# loop upto 5 starting from 2
print("\n")
for x in range(2, 5):
  print(x)

# Step increase
print("\n")
for x in range(2, 21, 2):
  print(x)

# using else in loop to print message once loop finished
print("\n")
for x in range(5):
  print(x)
else:
  print("Bye bye!")