"""
Let's Play with Object and its Properties
1. Modify
2. Delete properties
3. Delete Object
"""

class Demo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("Hello Dear " + self.name)

obj = Demo("Raj", 28)
obj.greeting()
print("Raj is ", obj.age, "years old")

# Modify Object Properties
obj.age = 30
print("Age modified to :",obj.age)

# Delete Object Properties
del obj.age
# Will throw an error
print(obj.age)  # AttributeError: 'obj' object has no attribute 'age'

# Delete Objects
del obj
# Will throw an error
print(obj)      # NameError: 'obj' is not defined