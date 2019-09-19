letter = input("Input a letter of the alphabet: ")

if letter in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % letter)
elif letter == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % letter)