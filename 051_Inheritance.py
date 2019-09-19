# Super Class / Parent Class
class A:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def greeting(self):
    print("Hello", self.firstname, self.lastname)

# Sub Class / Child Class
class B(A):
  pass

# Driver Code
x = B("Raj", "Bhagwat")
x.greeting()
