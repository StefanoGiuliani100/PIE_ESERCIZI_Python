class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

class User:
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}-year-old {self.gender} from {self.location}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# 9-1
restaurant = Restaurant("The Italian Place", "Italian")
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2
restaurant1 = Restaurant("The French Place", "French")
restaurant2 = Restaurant("The Chinese Place", "Chinese")
restaurant3 = Restaurant("The Mexican Place", "Mexican")

restaurants = [restaurant1, restaurant2, restaurant3]

for restaurant in restaurants:
    restaurant.describe_restaurant()

# 9-3
user1 = User("John", "Doe", 25, "male", "New York")
user2 = User("Jane", "Doe", 30, "female", "Los Angeles")
user3 = User("Bob", "Smith", 40, "male", "Chicago")

users = [user1, user2, user3]

for user in users:
    user.describe_user()
    user.greet_user()