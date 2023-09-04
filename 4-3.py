# Make a list of the numbers from one to one million, and then use a for loop to print the numbers
numbers = list(range(1, 10000))


# Make a list of the numbers from one to one million
numbers = list(range(1, 1000001))

# Use min() and max() to make sure your list actually starts at one and ends at one million
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))

# Use the sum() function to see how quickly Python can add a million numbers
print("Sum of numbers:", sum(numbers))

# Use the third argument of the range() function to make a list of the odd numbers from 1 to 20
odd_numbers = list(range(1, 21, 2))

# Use a for loop to print each number
for number in odd_numbers:
    print(number)

