# Create a list of countries
countries = ['Japan', 'Iceland', 'New Zealand', 'Peru', 'Egypt']

# Use len() to print the number of countries in the list
print("Number of countries:", len(countries))

# Use append() to add a new country to the end of the list
countries.append('Australia')

# Use insert() to add a new country to the beginning of the list
countries.insert(0, 'Canada')

# Use pop() to remove the last country from the list and print it
last_country = countries.pop()
print("Last country:", last_country)

# Use remove() to remove a specific country from the list
countries.remove('Peru')

# Use sort() to sort the list in alphabetical order
countries.sort()

# Use reverse() to reverse the order of the list
countries.reverse()

# Use a for loop to print each country in the list
print("Countries:")
for country in countries:
    print(country)

# Use a list comprehension to create a new list of the first two letters of each country
first_two_letters = [country[:2] for country in countries]
print("First two letters of each country:", first_two_letters)