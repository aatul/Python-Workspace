"""
Finally Clause

Think of a task you will always want your program to do, whether it runs perfectly or raise any kind of error. 

“finally” is used to perform clean up actions, and will be executed under all conditions.

Before leaving the try statement, “finally” clause is always executed, whether any exception is raised or not. 

Whenever an exception occurs and is not being handled by the except clause, first finally will occur and then the error is raised as default
"""

def divide(a, b): 
	try: 
		result = a / b 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero") 
	else: 
		print("Yeah ! Your answer is :", result) 
	finally: 
		print("I'm finally clause, always raised !!") 

# Driver Code
# Look at parameters and note the working of Program 
divide(3, 1)
divide(3, 3)
divide(3, 0)