# Python Palindromes
entered_string = input("Enter a Palindrome - ")
string_array = list(entered_string)
reversed_string = string_array.copy()
# array_length
# array_iterator
length_of_string = 0
for value in string_array:
    length_of_string += 1
for value in string_array:
        reversed_string[length_of_string - 1] = value
        length_of_string = length_of_string - 1
        
string_array = ''.join(string_array)
reversed_string = ''.join(reversed_string)

if string_array == reversed_string:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

