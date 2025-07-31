alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#6-7
person_1 = {
    'first_name': 'marko',
    'last_name': 'markovic',
    'age': 24,
    'city': 'spodnji duplek'
}

person_2 = {
    'first_name': 'elvis',
    'last_name': 'druzic',
    'age': 17,
    'city': 'zgornji duplek'
}

person_3 = {
    'first_name': 'branka',
    'last_name': 'brankovski',
    'age': 47,
    'city': 'mozirje'
}

peoples = [person_1, person_2, person_3]

for people in peoples:
    for key, value in people.items():
        print(f"{key}: {value}")

#6-8
pet_1 = {
    "name": "a",
    "species": "a",
    "age": 1,
    "owner": "a"
}
pet_2 = {
    "name": "b",
    "species": "b",
    "age": 2,
    "owner": "b"
}
pet_3 = {
    "name": "c",
    "species": "c",
    "age": 3,
    "owner": "c"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")