# Define a tuple
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Initialize counter
count_odd = 0
count_even = 0

# Let's loop through tuple now
for x in numbers:
        if not x % 2: 
    	     count_odd+=1
        else:
    	     count_even+=1

print("Total even numbers : ", count_even)
print("Total odd numbers : ", count_odd)