#5-3 to 5-5
alien_color = 'green'
points = 0

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print(f"You earned {points} points.")

#5-6
age = 77
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

print(f"You're {stage}.")

#5-7 - kinda
favorite_fruits = ['banana', 'strawberry', 'mango']
for fruit in favorite_fruits:
    if fruit in ['banana', 'strawberry', 'kiwi']:
        print(f"You also like {fruit}!")
    else:
        print(f"Ewww, {fruit} is gross!")

some_list = [2]
if some_list:
    print('1')
else:
    print('0')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping} to your pizza.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

#5-8, 5-9
user_names = ['jake', 'blake', 'nathan', 'justin', 'sully', 'admin']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user_name.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

#5-10
current_users = ['jake', 'blake', 'nathan', 'justin', 'sully', 'admin']
new_users = ['oni', 'recca', 'morbot', 'Blake', 'nathan']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, but username {new_user} already exists, please pick a new one.")
    else:
        print(f"Username {new_user} is available.")

#5-11
numbers = [number for number in range(1, 10)]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")