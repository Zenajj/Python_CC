from car import Car, ElectricCar
from restaurant import Restaurant, IceCreamStand
from random import randint, choice

class Die:
    """
    Exercise 9-13
    Create dice.
    """
    def __init__(self, sides=6):
        """Initialize Die"""
        self.sides = sides
    
    def roll_die(self):
        """Print random number between 1 and sides"""
        print(f"Rolling {self.sides}-sided die: {randint(1, self.sides)}")

#Exercise 9-14:
lottery_choices = ("2", "3", "7", "9", "13", "15", "18", "21", "26", "29", "a", "g", "r", "z", "o")
winning_choices = []
for item in range(4):
    winning_choices.append(choice(lottery_choices))
print(winning_choices)


new_die_6 = Die()
new_die_10 = Die(10)
new_die_20 = Die(20)

for die in range(10):
    new_die_6.roll_die()
for die in range(10):
    new_die_10.roll_die()
for die in range(10):
    new_die_20.roll_die()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

bosancek = IceCreamStand("bosancek", "slascicarna", "pistacija", "vanilija", "cokolada")
bosancek.print_flavours()

restaurant = Restaurant("Han", "Chinese")
restaurant.open_restaurant()
restaurant.describe_restaurant()
print(f"customers served: {restaurant.number_served}")
restaurant.set_number_served(29)
print(f"customers served: {restaurant.number_served}")
restaurant.increment_number_served(10)
print(f"customers served: {restaurant.number_served}")