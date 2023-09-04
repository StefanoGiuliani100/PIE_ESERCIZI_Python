# Use a variable to represent a person's name
name = "Eric"

# Print a message to that person
print(f"Hello {name}, would you like to learn some Python today?")

# Print the name in lowercase
print(name.lower())

# Print the name in uppercase
print(name.upper())

# Print the name in title case
print(name.title())

# Represent the famous person's name using a variable
famous_person = "Albert Einstein"

# Compose the message using the famous person's name and the quote
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

# Print the message
print(message)

# Use a variable to represent a person's name with whitespace characters
name = "\t  Eric\n  "

# Print the name with whitespace
print(f'Name with whitespace: "{name}"')

# Print the name with leading whitespace removed
print(f'Name with leading whitespace removed: "{name.lstrip()}"')

# Print the name with trailing whitespace removed
print(f'Name with trailing whitespace removed: "{name.rstrip()}"')

# Print the name with all whitespace removed
print(f'Name with all whitespace removed: "{name.strip()}"')