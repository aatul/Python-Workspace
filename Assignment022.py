# String Palindrome

str = input("Enter the string : ")

# Reverse string
rev = str[::-1]

if (str == rev): 
    print("String is Palindrome")
else:
    print("String is not Palindrome")