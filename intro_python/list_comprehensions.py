# How list comprehensions is organized
#list_variable = [for x in x iterable_value]
list_variable = [str(x) + " Billy" for x in range(1,30)]
print(list_variable)

# Splitting Letters in a string
split_letters = []
for letters in "billyotieno":
    split_letters.append(letters)
    
print(split_letters)

# Creating list with conditions
list_of_fish = ('blowfish', 'clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in list_of_fish if fish != 'octopus']
print(fish_list)

# Mathematical number list -- List comprehension
# Square all even numbers between 0 and 10
number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

# Nested if statements with a list comprehension
number_list_hundred = [x for x in range(0, 100) if x % 3 == 0 if x % 2 == 0]
print(number_list_hundred)

new_list = [x for x in range(5)]
print(new_list)

#new assignment trick in town..... For assigning values into lists..
mango, banana, oranges, swoosh, watermelon = new_list
print(mango)
print(banana)
print(oranges)
print(swoosh)
print(watermelon)

# index(), sort(), append(), insert()