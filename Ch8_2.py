import pizza as p
from printing_models import print_models as pm
from printing_models import show_completed_models

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'mozzarela')

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
show_completed_models(completed_models)

#8-14
def make_car(manufacturer, model, **kwargs):
    """store car info"""
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
for key, value in car.items():
    print(f"{key}: {value}")
#8-12
def sandwich(*items):
    """print items in a sandwich"""
    for item in items:
        print(f"{item}")
sandwich("cheese","ham", "pickles")
#8-9
def show_messages(messages):
    """Show messages."""
    for message in messages:
        print(message)

sms_messages = ["m1", "m2", "m3", "m4"]
show_messages(sms_messages)

#8-10
def send_messages(messages, sent_messages):
    """Sends messages and prints them out."""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

sent_messages = []
send_messages(sms_messages, sent_messages)
print("sms_messages:")
show_messages(sms_messages)
print("sent_messages:")
show_messages(sent_messages)

def print_models(unprinted_designs, completed_models):
    """
    imulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def greet_users(names):
    """Print a greeting for each user in a list."""
    for name in names:
        print(f"Hello {name.title()}!")

usernames = []
for username in range(1,6):
    usernames.append(f"user_{username}")
greet_users(usernames)