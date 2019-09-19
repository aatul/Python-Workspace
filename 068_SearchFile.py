"""
Serach File in Current Folder:

WAP to search '.txt' files in current folder.

We can change file type/name and path according to the requirements. 
"""

import os 

# Get the directory that the program is currently running in
dir_path = os.path.dirname(os.path.realpath(__file__)) 

for root, dirs, files in os.walk(dir_path): 

	for file in files: 

		# Change the extension from '.txt' to the one of your choice
		if file.endswith('.txt'): 
			print(root + "/" + str(file))
