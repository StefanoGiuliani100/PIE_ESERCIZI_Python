def display_message():
    print("In this chapter, I am learning about functions in Python.")

display_message()

def favorite_book(title):
    print("One of my favorite books is " + title + ".")

favorite_book("The Great Gatsby")

def make_shirt(size, message):
    print("The shirt size is " + size + " and the message printed on it is " + message + ".")

make_shirt("L", "Hello World!")

def make_shirt(size="large", message="I love Python"):
    print("The shirt size is " + size + " and the message printed on it is " + message + ".")

make_shirt()
make_shirt(size="medium")
make_shirt(message="Hello World!")

def describe_city(city, country="USA"):
    print(city + " is in " + country + ".")

describe_city("New York City")
describe_city("Paris", "France")
describe_city("Los Angeles")

def city_country(city, country):
    return city + ", " + country

print(city_country("New York City", "USA"))
print(city_country("Paris", "France"))
print(city_country("Los Angeles", "USA"))


def make_album(artist_name, album_title, number_of_tracks=""):
    album = {"artist": artist_name, "title": album_title}
    if number_of_tracks:
        album["tracks"] = number_of_tracks
    return album

print(make_album("Taylor Swift", "1989"))
print(make_album("The Beatles", "Abbey Road", 17))
print(make_album("Kendrick Lamar", "To Pimp a Butterfly"))

def make_album(artist_name, album_title, number_of_tracks=""):
    album = {"artist": artist_name, "title": album_title}
    if number_of_tracks:
        album["tracks"] = number_of_tracks
    return album

while True:
    print("\nEnter the album information:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    tracks = input("Number of tracks (optional): ")
    if tracks == 'q':
        break

    album = make_album(artist, title, tracks)
    print(album)


def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hello, how are you?", "What are you up to?", "How's the weather?"]
show_messages(messages)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print("Sending message: " + current_message)
        sent_messages.append(current_message)

messages = ["Hello, how are you?", "What are you up to?", "How's the weather?"]
sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print("Messages: " + str(messages))
print("Sent messages: " + str(sent_messages))

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print("Sending message: " + current_message)
        sent_messages.append(current_message)

def show_messages(sent_messages):
    print("\nShowing all sent messages:")
    for message in sent_messages:
        print(message)

messages = ["Hello, how are you?", "What are you up to?", "How's the weather?"]
sent_messages = []
send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print("\nFinal lists:")
print("Messages: " + str(messages))
print("Sent messages: " + str(sent_messages))