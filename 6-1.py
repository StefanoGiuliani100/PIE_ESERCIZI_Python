rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())