# define values
a = 10
b = 20
c = 30

# if statement
if b > a:
  print("b is greater than a")
  print("Hi")
  print("Hello")

# if - else statement
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

# if - else if statement
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# if - else if - else statement
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand if
# if you want to execute single statement
if a > b: print("a is greater than b")

# Short Hand if - else
print("a is greater than b") if a > b else print("b is greater than a")

# Short Hand if - multiple else, similar to else if and else ladder
print("a is greater") if a > b else print("=") if a == b else print("b is greater")

# using 'and' keyword
if b > a and c > a:
  print("Both b and c are greater than a")

# using 'or' keyword
if b > a or b > c:
  print("c may be greater than a & b")