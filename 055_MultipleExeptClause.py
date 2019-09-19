"""
Multiple Except Clause

A try statement can have more than one except clause, to specify handlers for different exceptions. Please note that at most one handler will be executed.
"""
# Program to handle multiple errors with one except statement 
try : 
	a = 3
	if a < 4 : 
		# throws ZeroDivisionError for a = 3 
		b = a/(a-3) 
        # throws NameError if a >= 4 
	
	print ("Value of b = ", b)

# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
	print ("Error Occurred and Handled")

"""
Let's try this too:

Change the value of ‘a’  to check different output
"""