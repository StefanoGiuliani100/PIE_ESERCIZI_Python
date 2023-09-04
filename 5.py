car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Tests for equality and inequality with strings
string1 = "hello"
string2 = "world"
print(string1 == string2)  # False
print(string1 != string2)  # True

# Tests using the lower() method
string3 = "HELLO"
string4 = "hello"
print(string3.lower() == string4)  # True
print(string3 == string4)  # False

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
num1 = 10
num2 = 5
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)  # True
print(num1 < num2)  # False
print(num1 >= num2)  # True
print(num1 <= num2)  # False

# Tests using the and keyword and the or keyword
num3 = 7
print(num1 > num2 and num3 < num2)  # False
print(num1 > num2 or num3 < num2)  # True

# Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)  # True
print('grape' in fruits)  # False

# Test whether an item is not in a list
print('apple' not in fruits)  # False
print('grape' not in fruits)  # True