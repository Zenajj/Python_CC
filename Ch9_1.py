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
    Exercise 9-1
    Create class and print  a message indicating that the restaurant is open
    """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cousine type."""
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print restaurant attributes."""
        print(f"\nRestaurant name: {self.name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        """ Method prints a message indicating that the restaurant is open."""
        print(f"\nRestaurant {self.name}, is now open.")

class User:
    """
    Exercise 9-3
    Create user
    """

    def __init__(self, first_name, last_name, email, password, country):
        """Initialize user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.country = country
    
    def describe_user(self):
        """Prints a summary of the user's information"""
        print(f"\nUser name: {self.first_name.title()} {self.last_name.title()}")
        print(f"E-mail: {self.email}")
    
    def greet_user(self):
        """Greets user."""
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

ana = User("Ana", "banana", "anabanana@anana.si", "12345", "Slovenija")
ana.describe_user()
ana.greet_user()

restaurant = Restaurant("Han", "Chinese")
restaurant.open_restaurant()
restaurant.describe_restaurant()

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

