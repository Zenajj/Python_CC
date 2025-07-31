#8-7
def make_album(artist_name, album_title, number_of_songs = None):
    """Builds a dictionary, describing an album."""
    album = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album
print(make_album('dfsgds', 'eerere'))
print(make_album('dfsgds', 'eerere', 7))

#8-8
while True:
    print("Create new album, enter 'q' at any time to quit.")
    artist = input("Enter artist name: ")
    if artist == "q":
        break

    title = input("Enter album title: ")
    if title == "q":
        break

    songs = input("Number of songs(0 if unknown): ")
    if songs == "q":
        break
    if songs == "":
        songs = 0
    songs = int(songs)
    if songs == 0:
        songs = None
        
    album = make_album(artist, title, songs)
    if songs:
        print(f"{album['album_title'].title()}, by {album['artist_name'].title()} ({album['number_of_songs']} songs)")
    else:
        print(f"{album['album_title'].title()}, by {album['artist_name'].title()}")

#8-6
def city_country(city, country):
    """Returns formated string of a city and an country."""
    formated_city_country = f"{city.title()}, {country.title()}"
    return formated_city_country
print(city_country('kamnik', 'slovenija'))

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def build_person(first_name, last_name,  age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', 27)
musician2 = build_person('oto', 'pestner')
print(musician)
print(musician2)

def get_formatted_name(first_name, last_name, middle_name = ""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
musician2 = get_formatted_name('jimi', 'hendrix')
print(musician)
print(musician2)

#8-3
def make_shirt(message, size="L"):
    """provide information for a shirt."""
    print(f"\nSize: {size}")
    print(f"Message: {message}")
make_shirt("top shirt")
make_shirt(message = "big boy", size = "S")

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet('sultan')

def favorite_book(title):
    '''Function tells everyone about my favourite book.'''
    print(f"One of my favorite books is {title.title()}.")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")
#book_title = input("What's your favourite book? ")
#favorite_book(book_title)
#user_name = input("Your username: ")
#greet_user(user_name)