class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

class Restaurant:
    """
    Exercise 9-1, 9-4
    Create class and print  a message indicating that the restaurant is open
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cousine type."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print restaurant attributes."""
        print(f"\nRestaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        """ Method prints a message indicating that the restaurant is open."""
        print(f"\nRestaurant {self.name}, is now open.")
    
    def set_number_served(self, customers):
        """Set the number of customers that have been served"""
        self.number_served = customers
    
    def increment_number_served(self, served):
        """Increment the number of customers who've been served"""
        self.number_served += served

class User:
    """
    Exercise 9-3, 9-5
    Create user
    """

    def __init__(self, first_name, last_name, email, password, country):
        """Initialize user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.country = country
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\nUser name: {self.first_name.title()} {self.last_name.title()}")
        print(f"E-mail: {self.email}")
    
    def greet_user(self):
        """Greets user."""
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        self.login_attempts = 0

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(28)
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

ana = User("Ana", "banana", "anabanana@anana.si", "12345", "Slovenija")
ana.describe_user()
print(ana.login_attempts)
ana.increment_login_attempts()
ana.increment_login_attempts()
print(ana.login_attempts)
ana.reset_login_attempts()
print(ana.login_attempts)
ana.greet_user()

restaurant = Restaurant("Han", "Chinese")
restaurant.open_restaurant()
restaurant.describe_restaurant()
print(f"customers served: {restaurant.number_served}")
restaurant.set_number_served(29)
print(f"customers served: {restaurant.number_served}")
restaurant.increment_number_served(10)
print(f"customers served: {restaurant.number_served}")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()