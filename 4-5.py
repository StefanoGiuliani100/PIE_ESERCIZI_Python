# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foods = ('pizza', 'pasta', 'burger', 'fries', 'salad')

# Use a for loop to print each food the restaurant offers.
print("Foods offered:")
for food in foods:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
# This will result in a TypeError because tuples are immutable.
# foods[0] = 'sandwich'

# The restaurant changes its menu, replacing two of the items with different foods.
# Add a line that rewrites the tuple.
foods = ('sandwich', 'pasta', 'hot dog', 'fries', 'soup')

# Use a for loop to print each food the restaurant offers.
print("\nNew foods offered:")
for food in foods:
    print(food)