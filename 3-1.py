# Start with the list from Exercise 3-6
guests = ['Malala Yousafzai', 'Albert Einstein', 'Nikola Tesla', 'Ruth Bader Ginsburg', 'Maya Angelou', 'Ada Lovelace']

# Print a message saying that we can invite only two people for dinner
print("Sorry, we can invite only two people for dinner.")

# Use pop() to remove guests from the list one at a time until only two names remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, we can't invite you to dinner.")

# Use a for loop to print a message to each of the two people still on our list
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner.")

# Use len() to print a message indicating the number of people we're inviting to dinner
num_guests = len(guests)
print(f"We're inviting {num_guests} people to dinner.")

# Use del to remove the last two names from our list, so we have an empty list
del guests[0]
del guests[0]

# Print the list to make sure we actually have an empty list at the end of our program
print(guests)

