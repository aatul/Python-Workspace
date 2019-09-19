# Take input
str = input("Input a word to reverse: ")

# loop
for char in range(len(str) - 1, -1, -1):
  print(str[char], end="")

print("\n")