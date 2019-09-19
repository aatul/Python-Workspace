"""
User-defined Exceptions

A user can create his own run-time error or exception using Exception class.

Programmers may name their own exceptions by creating a new exception class. 

Exceptions need to be derived from the Exception class, either directly or indirectly.

One can also derive any built-in or standard Exception class such as ZeroDivisionError.

Although not mandatory, most of the exceptions are named as names that end in “Error” similar to naming of the standard exceptions in python.
"""

# A python program to create user-defined exception 
# class NegativeNumberException is derived from super class Exception 
class NegativeNumberException(Exception): 

	# Constructor or Initializer 
	def __init__(self, value): 
		self.value = value 

	# __str__ is to print() the value 
	def __str__(self): 
		return(repr(self.value)) # repr() = str()

def factorial(n):  
   if n < 0:
        try: 
	        raise(NegativeNumberException(n)) 
        # Value of Exception is stored in error 
        except NegativeNumberException as error: 
            print('A New Exception occured:',error.value)
   elif n == 1:  
       return n  
   else:  
       return n*factorial(n-1)  

# Driver Code
num = int(input("Enter a number: ")) 
print("The factorial of",num,"is",factorial(num))
