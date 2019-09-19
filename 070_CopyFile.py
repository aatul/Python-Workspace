"""
The system() method allows you to instantly execute any OS command or a script in the subshell.

You need to pass the command or the script as an argument to the system() call. Internally, this method calls the standard C library function.

Its return value is the exit status of the command.
"""

import os

# Syntax Command OldFileName NewFileName
os.system('copy demo3.txt demo5.txt')