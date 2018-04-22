# Except is important for input validation..
def div23by(divideby):
    try:
        return 23/divideby
    except ZeroDivisionError:
        print("Error you tried to divide by zero")

print(div23by(2))
print(div23by(0))
print(div23by(5))