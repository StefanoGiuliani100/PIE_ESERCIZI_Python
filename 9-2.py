from random import randint

class Die:
    """Represent a die, which can be rolled."""
    
    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides
    
    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die and roll it 10 times.
d6 = Die()
for roll_num in range(10):
    print(d6.roll_die())

# Make a 10-sided die and roll it 10 times.
d10 = Die(sides=10)
for roll_num in range(10):
    print(d10.roll_die())

# Make a 20-sided die and roll it 10 times.
d20 = Die(sides=20)
for roll_num in range(10):
    print(d20.roll_die())


import random

# Make a list or tuple containing a series of 10 numbers and 5 letters.
ticket = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e']

# Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
winning_ticket = []
while len(winning_ticket) < 4:
    pulled_item = random.choice(ticket)
    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)

print("\nThe final winning ticket is:", winning_ticket)


import random

# Make a list or tuple called my_ticket.
my_ticket = [1, 2, 3, 4, 5, 6]

# Write a loop that keeps pulling numbers until your ticket wins.
num_tickets = 0
while True:
    num_tickets += 1
    winning_ticket = []
    while len(winning_ticket) < len(my_ticket):
        pulled_item = random.randint(1, 10)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    # Print a message reporting how many times the loop had to run to give you a winning ticket.
    if my_ticket == winning_ticket:
        print(f"Congratulations! You won the lottery in {num_tickets} tries!")
        break