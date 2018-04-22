def studentages(a, b, c, d):
    return a, b, c, d

my_list = [12, 23, 31, 44]

# studentages(my_list)

# Concept learned today - unpacking in python
studentages(*my_list)
print(studentages(*my_list))

# For list you use * for dictionaries use **
def studentagesdict(a, b, c):
    return a, b, c

my_dict = {'a':'billy',
           'b':'otiened',
           'c':'collaboration'}

studentagesdict(**my_dict)
print(studentagesdict(**my_dict))