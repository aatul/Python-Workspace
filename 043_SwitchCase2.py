# Implement Switch Case Statement using Dictionary

def monday():
    return "Monday"
def tuesday():
    return "Tuesday"
def wednesday():
    return "Wednesday"
def thursday():
    return "Thursday"
def friday():
    return "Friday"
def saturday():
    return "Saturday"
def sunday():
    return "Sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

# Driver Code
print(switch(1))
print(switch(0))