#7-5
wellcom_message = "Hello, and wellcome to out theater!"
wellcom_message += "\nHow old are you? "
age = int(input(wellcom_message))
ticket_price = 0

if age < 3:
    ticket_price = 0
elif age < 12:
    ticket_price = 10
else:
    ticket_price = 15
print(f"Cost of your ticket is €{ticket_price}.")

prompt = "Tell me something, and I'll repeat it back to you:"
prompt += "\nType 'quit' to end the program: "
message = ""

while True:
    message = input(prompt)
    if message != 'quit':
        print(message)
        continue
    break

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

prompt = "Tell me something, and I'll repeat it back to you2:"
prompt += "\nType 'quit' to end the program: "
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#7-3
number = input("enter a number: ")
number = int(number)
if number % 10 == 0:
    print("it's multiple of 10.")
else:
    print("It's not multiple of 10.")

#7-2
persons_nr = input("Hello, how many people do you need to reserve dining spot for? ")
persons_nr = int(persons_nr)
if persons_nr > 8:
    print("You'll have to wait.")
else:
    print("Table's ready.")

#7-1
car = input("Hello, what brand of car would you like? ")
print(f"Let me see if I can find you a {car}.")

prompt_name = "If you share your name, we can personalize the messages you see."
prompt_name += "\nWhat is your first name? "
prompt_age = "How old are you? "

name = input(prompt_name)
age = input(prompt_age)

if int(age) >= 18:
    print(f"\nHello, {name.title()}, you can enter!")
else:
    print(f"Sorry, {name}, only adults can enter, and you are {18 - int(age)} years too young!")


