def favorite_book(title):
    '''Function tells everyone about my favourite book.'''
    print(f"One of my favorite books is {title.title()}.")

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello {username.title()}!")

book_title = input("What's your favourite book? ")
favorite_book(book_title)
user_name = input("Your username: ")
greet_user(user_name)