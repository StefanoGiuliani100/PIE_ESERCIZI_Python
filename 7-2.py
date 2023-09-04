# Using a conditional test in the while statement to stop the loop
toppings = []
topping = ''
while topping != 'quit':
    topping = input("What topping would you like on your pizza? Enter 'quit' when you are finished: ")
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
        toppings.append(topping)
print(f"Your pizza will have the following toppings: {', '.join(toppings)}.")

# Using an active variable to control how long the loop runs
active = True
while active:
    age = input("How old are you? Enter 'quit' when you are finished. ")
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("You get in free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

# Using a break statement to exit the loop when the user enters a 'quit' value
toppings = []
while True:
    topping = input("What topping would you like on your pizza? Enter 'quit' when you are finished: ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
    toppings.append(topping)
print(f"Your pizza will have the following toppings: {', '.join(toppings)}.")