# Define While Loop
i = 1         # Initialization
while i < 6:  # Condition
  print(i)
  i += 1      # Increment / Decrement

# Using break statement in While Loop
print()
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Using continue statement in While Loop
print()
j = 0
while j < 6:
  if j == 3:
    continue
  print(j)
  j += 1