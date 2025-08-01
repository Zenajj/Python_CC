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