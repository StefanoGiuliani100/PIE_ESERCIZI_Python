sandwich_orders = ['BLT', 'turkey', 'roast beef', 'pastrami', 'pastrami', 'veggie']
finished_sandwiches = []

print("Welcome to the deli!")
print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nHere are the sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)