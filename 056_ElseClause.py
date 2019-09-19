"""
Else Clause

In python, you can also use else clause on try-except block which must be present after all the except clauses.

The code enters the else block only if the try clause does not raise an exception.
"""

# Function which returns a/b 
def divide(a,b):
    try:
        c=(a/b)
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print(c)

# Driver program to test above function 
divide(6.0, 3.0) 
divide(6.0, 0.0) 
