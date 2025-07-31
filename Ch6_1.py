alien_0 = {
    'color': 'green',
    'points': 5
    }

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
color_value = alien_0.get('color')
print(color_value)

#6-1
person = {
    'first_name': 'marko',
    'last_name': 'markovic',
    'age': 24,
    'city': 'spodnji duplek'
}

for key in person:
    print(person[key])

for key, value in person.items():
    print(f"{key}: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    if name in friends:
        print(name.title())

# To display only distinct values:
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

#6-5
rivers = {
    'nile': 'egypt',
    'sava': 'slovenia',
    'amazon': 'brazil',
}

for river, country in rivers.items():
    print(f"River {river.title()} flows through {country.title()}.")