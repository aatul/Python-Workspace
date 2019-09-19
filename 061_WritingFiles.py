"""
Write to an Existing File

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""

# Open and append file
f1 = open("demo.txt", "a")
f1.write("Now the data is appended in file!")
f1.close()

# Open and read the file after the appending:
f2 = open("demo.txt", "r")
print(f2.read())

# Overwrite the file
f3 = open("demo2.txt", "w")
f3.write("Sorry! The original file is overwritten!")
f3.close()

#open and read the file after overwriting file:
f4 = open("demo2.txt", "r")
print(f4.read())

# To write multiple lines to a file, use:
f5 = open("demo3.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
f5.writelines(lines_of_text)
f5.close()

#open and read the file after the writing multiple lines:
f6 = open("demo3.txt", "r")
print(f6.read())