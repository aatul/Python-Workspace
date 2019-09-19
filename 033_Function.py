# Define a function
def func1():
  print("Hello this is function")
  print("Demo function")

# Calling a Function
func1()

# Creating parameterized function
def func2(name):
  print("Hello " + name)
# Calling a Function
func2("Raj")

# Setting default value for parameter
def func3(name = "Raj"):
  print("I am " + name)
func3("Aatul")
func3()   # Will use Raj as default value

# Passing multiple values 
def func4(a, b): 
	print("a:", a) 
	print("b:", b) 
func4(10,20) 

# Passing multiple values as Keyword arguments
def func5(a, b): 
	print("a:", a) 
	print("b:", b) 
func5(a=10,b=20) 

# Passing List as a parameter
def func6(lang):
  for x in lang:
    print(x)
# Driver Code
list1 = ["Java","C","CPP","Android","HTML","Dart","Go"] 
func6(list1)

# Define Empty Function
# Incorrect empty function in Python -> def emptyFun():   
# Here is correct way to define empty function
def emptyFun():  
    pass
