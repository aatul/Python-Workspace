"""
Variable length arguments:

We can have both normal and keyword variable number of arguments
"""

# *args for variable number of arguments 
def func8(*argv):  
    for x in argv:  
        print (x) 
        
# Driver code to test above code
func8('Hello', 'This', 'is', 'Python', '3')
print()
func8('Hi','This','is','Python')

# **keyargs for variable number of keyword arguments 
def myFun(**keyargs):  
    for key, value in keyargs.items(): 
        print ("%s == %s" %(key, value)) 
        
# Driver code to test above code
myFun(first ='Beginner', mid ='Intermediate', last='Expert')