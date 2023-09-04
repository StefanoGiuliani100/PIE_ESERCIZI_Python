def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('peanut butter', 'jelly')

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)