"""
File Handling

The main function for handling files in Python is the open() function.

The open() function takes two parameters; filename, and mode of opening a file.

There are four different methods (modes) for opening a file:

1. "r" - Read - Default value. Opens a file for reading, throws an error if the file does not exist

2. "a" - Append - Opens a file for appending, creates the file if it does not exist

3. "w" - Write - Opens a file for writing, creates the file if it does not exist

4. "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode:

1. "t" - Text - Default value. Text mode

2. "b" - Binary - Binary mode (e.g. images)

"""

# Open a file for reading
f1 = open("demo.txt")

# Read contents of file
print(f1.read())

# Read part of the file
# Read first 10 characters of file
f2 = open("demo.txt", "r")
print(f2.read(10))

# Read one line of the file
f3 = open("demo.txt", "r")
print(f3.readline())

# Loop through file
f4 = open("demo.txt", "r")
for x in f4:
  print(x)

# Close file
f1.close()
f2.close()
f3.close()
f4.close()