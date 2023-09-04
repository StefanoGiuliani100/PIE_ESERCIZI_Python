car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")


group_size = int(input("How many people are in your dinner group? "))
if group_size > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

number = int(input("Give me a number, please: "))
if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")