# Super Class / Parent Class
class A:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def greeting(self):
    print("Hello", self.firstname, self.lastname)

# Sub Class / Child Class
class B(A):
  def __init__(self, fname, lname):
    # If Super init() is not called, will operride super init()
    A.__init__(self, fname, lname) 
    self.age = 28
    self.city = "Nagpur"

# Driver Code
x = B("Raj", "Bhagwat")
x.greeting()
print("Age:",x.age)
print("City:",x.city)