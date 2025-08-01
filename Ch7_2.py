# Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)

#7-8, #7-9
print("7-8")
sandwich_orders = ["one", "pastrami","two", "pastrami", "pastrami","three", "pastrami","four"]
finished_sandwiches = []

print("We ran out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sendwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sendwich)
    print(f"I made {current_sendwich}.")

print(finished_sandwiches)