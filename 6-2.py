person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Bob',
    'last_name': 'Smith',
    'age': 40,
    'city': 'Chicago'
}

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(f"{key.title()}: {value}")
    print()