filename = input("Input the Filename: ")
list1 = filename.split(".") # returns a list
print(list1)
print ("The extension of the file is : " + repr(list1[1]))