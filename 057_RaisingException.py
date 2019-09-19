"""
Raise an Exception

The raise statement allows the us to force a specific exception to occur.

The sole argument in raise indicates the exception to be raised.

This must be either an exception instance or an exception class (a class that derives from Exception).

The output of the below code will simply line printed as “An exception” but a Runtime error will also occur in the last due to raise statement in the last line.
"""

# Program to raise an exception 
try: 
	raise NameError("Hi I am an raised Exception") # Raise Error 
except NameError: 
    print ("An exception")
    raise # To determine whether the exception was raised or not 
