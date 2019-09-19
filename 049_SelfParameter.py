"""
The self parameter is a reference to the current instance of the class similar to 'this' reference in Java, and is used to access variables that belong to the class.

It does not have to be named 'self', you can call it whatever you like such as 'obj' or 'abc', but it has to be the first parameter of any function in the class.

Previous Example =>
class Demo:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greeting(self):
    print("Hello Dear " + self.name)

obj = Demo("Raj", 28)
obj.greeting()
"""

class Demo:
  def __init__(object, name, age):
    object.name = name
    object.age = age

  def greeting(abc):
    print("Hello Dear " + abc.name)

obj = Demo("Raj", 28)
obj.greeting()