# Make a list of the multiples of 3 from 3 to 30
multiples_of_three = list(range(3, 31, 3))

# Use a for loop to print the numbers in your list
for number in multiples_of_three:
    print(number)

# Use a list comprehension to generate a list of the first 10 cubes
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)