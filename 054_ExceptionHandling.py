"""
Exception Handling

Like C++ & Java, Python also provides the exception handling with the help of try-except.

Some of the standard and most frequent exceptions are IndexError, ImportError, IOError, ZeroDivisionError, TypeError and FileNotFoundError.
 
Exception is the super/parent/base class for all the exceptions in Python.
"""

# Let us try to access the array element whose index is out of bound and handle the corresponding exception.
a = [1, 2, 3] 
try:  
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3]))
  
except IndexError: 
    print ("An error occurred")

print("The End")