""" Returning values from a method using tuple """

# This function returns a tuple 
def funTuple(): 
	str = "Java"
	x = 20
	return str, x 
	# Return tuple, we could also write (str, x) 

# Driver code to test above method 
str, x = funTuple() # Assign returned tuple 
print(str) 
print(x) 
print(funTuple())