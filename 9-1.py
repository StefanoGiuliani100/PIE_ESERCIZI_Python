class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant("Pizza Hut", "Italian")
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 10
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.set_number_served(20)
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.increment_number_served(5)
print(f"The restaurant has served {restaurant.number_served} customers.")


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("John", "Doe", 30, "Male")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Number of login attempts: {user.login_attempts}")