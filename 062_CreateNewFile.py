"""
Create a New File

To create a new file in Python, use the open() method, with one of the following parameters:

1. "x" - Create - will create a file, returns an error if the file exist

2. "a" - Append - will create a file if the specified file does not exist

3. "w" - Write - will create a file if the specified file does not exist
"""

# Create a new empty file
f1 = open("demo3.txt", "x")

# Create a new file if it does not exist
f2 = open("demo4.txt", "w")

# Create a new file if it does not exist
f3 = open("demo5.txt", "a")