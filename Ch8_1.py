def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")

user_name = input("Your username: ")
greet_user(user_name)