str = input("Input a string: ")

# initialize counter
digit=letter=0

for c in str:
    if c.isdigit():         # if digit or not
        digit=digit+1       # if digit, increment counter
        print("This is digit:",c)
    elif c.isalpha():
        letter=letter+1
        print("This is letter:",c)
    else:
        pass

print("Letters", letter)
print("Digits", digit)