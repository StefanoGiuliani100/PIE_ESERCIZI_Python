usernames = ['admin', 'jaden', 'john', 'sarah', 'mike']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username.title() + ", thank you for logging in again!")


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", thank you for logging in again!")
else:
    print("We need to find some users!")


current_users = ['jaden', 'john', 'sarah', 'mike', 'admin']
new_users = ['james', 'jane', 'sarah', 'mike', 'Jaden']

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("Sorry, " + user + " is already taken. Please enter a new username.")
    else:
        print("Great, " + user + " is still available.")


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")