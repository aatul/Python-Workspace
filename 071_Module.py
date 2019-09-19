"""
Modules in Python

Modules are primarily the (.py) files which contain Python code defining functions, class, variables, etc. with a suffix .py appended in its file name.

They can have different functions, variables, and classes in one file. We can also call them libraries.

A Python module brings certain benefits such as we can reduce redundancy in the code. It can let us maintain uniformity in the coding style.
"""

#we can write multiple modules in one import statement.
import math, random 

print (math.sqrt(625)) #prints square root of number 625

print (math.factorial(10)) #prints factorial of a number 10

print (math.pi) #prints value of pi according to the built-in module

print (random.randint(1,20)) #prints a random value from integers 1-20

print (dir(math)) #prints function name, variables, etc. in math module