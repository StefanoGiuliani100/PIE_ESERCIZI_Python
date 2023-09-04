person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

print("First Name: " + person['first_name'])
print("Last Name: " + person['last_name'])
print("Age: " + str(person['age']))
print("City: " + person['city'])


favorite_numbers = {
    'John': 5,
    'Jane': 10,
    'Bob': 15,
    'Alice': 20,
    'Mike': 25
}

for name, number in favorite_numbers.items():
    print(name + "'s favorite number is " + str(number))


# Define the glossary dictionary
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.'
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

# Add five more terms to the glossary
glossary['tuple'] = 'A collection of ordered, immutable elements.'
glossary['set'] = 'A collection of unique elements.'
glossary['function'] = 'A named block of code that performs a specific task.'
glossary['module'] = 'A file containing Python code that can be imported and used in other programs.'
glossary['class'] = 'A blueprint for creating objects that have specific attributes and methods.'

# Loop through the updated dictionary and print each key-value pair
for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")