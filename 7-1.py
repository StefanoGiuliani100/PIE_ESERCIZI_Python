toppings = []
while True:
    topping = input("What topping would you like on your pizza? Enter 'quit' when you are finished: ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to your pizza.")
    toppings.append(topping)
print(f"Your pizza will have the following toppings: {', '.join(toppings)}.")

while True:
    age = input("How old are you? Enter 'quit' when you are finished. ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("You get in free!")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")