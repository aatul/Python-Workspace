# Just loop
for x in range(16):
    if x % 3 == 0 and x % 5 == 0:
        print("Multiple of 3 & 5: ",x)
        continue
    elif x % 3 == 0:
        print("Multiple of 3: ",x)
        continue
    elif x % 5 == 0:
        print("Multiple of 5: ",x)
        continue
    print(x)