a = "Hello, World!"
print(a)
print(a[1])     # returns character from given index no.
print(a[2:5])   # returns substring with given start index and end index  
print(len(a))   # returns no. char in a string

print(a.split(",")) # separates words from string with given delimiter
c="Hello there lets have a skype meeting"
print(c.split(" "))

b = " Hello "
print(b)
print(b.strip())    # removes whitespaces from beggining and end

print(a.replace("H","Y"))   # replace old char with new char

print(a.lower())    # converts string to lower case
print(a.upper())    # converts string to upper case