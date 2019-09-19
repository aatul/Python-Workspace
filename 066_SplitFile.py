# Split words from each line using split() function 
with open("demo.txt", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split() 
        print(word)