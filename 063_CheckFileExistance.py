"""
Check if File exist

To avoid getting an error, you might want to check if the file exists before you try to delete it

You must import the OS module, and run its os.exist() function
"""

import os
if os.path.exists("demo3.txt"):
  print("The file exists")
else:
  print("The file does not exist")