import copy


new = dict()
value1 = {'name':'otieno',
          'age':'10',
          'honors':'firstclass',
          'height':'1500km'}
print(value1)

print(value1.keys())
print(value1.values())
print(value1.items())

# Iterating over a dictionary
new = value1
print(new)
new['name'] = 'Ochieng'
print(value1)

new_dict = copy.deepcopy(value1)
new_dict['name'] = "Alice"
print(new_dict)
print(new)

new_dict.get('name', 20)

# Ways to iterate over a dictionary

for i in new_dict:
    print(i, new_dict[i])
    
for i in value1.keys():
    print(value1[i])
    
for i in value1.values():
    print(i)
    
for i, j in value1.items():
    print(i, j, end=" ")