cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print(car == 'bmw')
print(car == 'Bmw')
print(car.title() == 'Bmw')
print(car != 'Bmw')

print('Numbers:')
age = 19
age_2 = 17
if age < 18:
    print('Underage')
if age == 18:
    print('18')
if age >= 18:
    print('You can vote')

if age >= 18 or age_2 >= 18:
    print("Both can come.")

print('Lists:')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
topping = 'pepperoni'
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('pepperoni' not in requested_toppings)

if topping in requested_toppings:
    print(f"We'll add {topping} on your pizza")
else:
    print(f"Sorry, we don't have {topping} as topping")

age = 23
if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $25.")
else:
  print("Your admission cost is $40.")

# better way to do it:
if age < 4:
  price = 0
elif age < 18:
  price = 25
else:
  price = 40

print(f"Your admission cost is ${price}.")