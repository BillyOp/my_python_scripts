#For loop
#Displaying lines concurrently

fh = open("details.txt") #Opens a file
#The for loop reads the number of lines in the file..
for line in fh.readlines():
    print(line, end="")
    
    
