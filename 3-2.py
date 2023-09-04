# Create a list of at least five places in the world you'd like to visit
places_to_visit = ['Japan', 'Iceland', 'New Zealand', 'Peru', 'Egypt']

# Print the list in its original order
print("Original order:")
print(places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the actual list
print("\nAlphabetical order:")
print(sorted(places_to_visit))

# Show that the list is still in its original order by printing it again
print("\nOriginal order:")
print(places_to_visit)

# Use sorted() to print the list in reverse-alphabetical order without changing the order of the original list
print("\nReverse-alphabetical order:")
print(sorted(places_to_visit, reverse=True))

# Show that the list is still in its original order by printing it again
print("\nOriginal order:")
print(places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()

# Print the list to show that its order has changed
print("\nReversed order:")
print(places_to_visit)

# Use reverse() to change the order of the list again
places_to_visit.reverse()

# Print the list to show that it's back to its original order
print("\nOriginal order:")
print(places_to_visit)

# Use sort() to change the list so it's stored in alphabetical order
places_to_visit.sort()

# Print the list to show that its order has been changed
print("\nAlphabetical order:")
print(places_to_visit)

# Use sort() to change the list so it's stored in reverse-alphabetical order
places_to_visit.sort(reverse=True)

# Print the list to show that its order has changed
print("\nReverse-alphabetical order:")
print(places_to_visit)