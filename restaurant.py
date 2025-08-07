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

class IceCreamStand(Restaurant):
    """
    Exercise 9-6
    Class for ice cream stands that adds flavours.
    """

    def __init__(self, restaurant_name, cuisine_type, *flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def print_flavours(self):
        """Display flavours that ice cream stand provides."""

        print(f"\nAvailable flavours at {self.name}:")
        for flavour in self.flavours:
            print(f"-{flavour}")