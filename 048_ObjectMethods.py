"""
Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.
"""

# Create a function that prints a greeting, and execute it on the object
class Demo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("Hello Dear " + self.name + ", it seems you are " + str(self.age))

obj = Demo("Raj", 28)
obj.greeting()