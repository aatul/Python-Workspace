# Implement Switch Case Statement using Class

class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"
 
    def case_2(self):
        return "Tuesday"
 
    def case_3(self):
        return "Wednesday"

s = PythonSwitch()

print(s.switch(1))
print(s.switch(0))