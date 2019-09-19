"""
Returning Multiple Values in Python
There are four ways to return multiple values in Python;

1. Using Object : 
Similar to C/C++ and Java, we can create a class to hold multiple values and return an object of the class.

2. Using Tuple : 
A Tuple is a comma separated sequence of items. It is created with or without (). Tuples are immutable.

3. Using List : 
A list is like an array of items created using square brackets. They are different from arrays as they can contain items of different types. Lists are different from tuples as they are mutable.

4. Using Dictionary :
A Dictionary is similar to hash or map in other languages. See this for details of dictionary.
"""

""" Returning values from a method using class """
class Test: 
	def __init__(self): 
		self.str = "Python"
		self.x = 20

# This function returns an object of Test 
def fun(): 
	return Test()  
	
# Driver code to test above method 
t = fun() 	# We can also write -> t = Test()
print(t.str) 
print(t.x) 
