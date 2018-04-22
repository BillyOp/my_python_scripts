#Learning Python Conditionals

a, b = 0, 1

if a < b:
    print("({}) is less than ({})" . format(a, b))
else:
    print("({}) is not less than ({})" . format(a, b))

#One liner conditional printer
#Similar to the other for loop
# a > b ? true : false   --- Sample simple Conditional

print("Foo" if a < b else "Bar")