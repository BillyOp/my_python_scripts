#Exception handling in python programming

try:
    fh = open('xlines.txt')
    for line in fh.readline():
        print(line)
except IOError as e:
    print("something bad happened ({})". format(e))
else:
    print("Do something instead")
    
print("After badness")