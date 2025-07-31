bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'kona']
print(bicycles[4].title())
print(bicycles[-2].title())
print(f"My first bicycle was a {bicycles[-1].title()}.")
bicycles[0] = 'rog'
print(f"My first bicycle was a {bicycles[0].title()}.")
print(bicycles)

#adding elt to a list
bicycles.append('trek')
print(bicycles)

#inserting
bicycles.insert(1, 'nakamura')
print(bicycles)

#removing - del
del bicycles[2]
print(bicycles)

#removing - pop
poped_bicycle = bicycles.pop()
print(bicycles)
print(poped_bicycle)
poped_bicycle = bicycles.pop(0)
print(bicycles)
print(poped_bicycle)

#removing - by value
bicycles.remove('redline')
print(bicycles)

#3-4
guests = ['mark marcus', 'ivan ivanovski', 'eluid eluidski', 'vladimir tepes']
for guest in guests:
    print(f"Hello {guest.title()}! \nYou are invited to a dinner.\n")

#3-5
print(f"Sadly, {guests[1].title()} can't make it to a dinner :(.")
del guests[1]
guests.append('ivana ivanovska')
for guest in guests:
    print(f"Hello {guest.title()}! \nYou are invited to a dinner.\n")

#3-6
print("I found a bigger table, and will invite more people :)")
guests.insert(0, 'john jordan')
guests.insert(2, 'rocky rocks')
guests.append('tom tomsky')
for guest in guests:
    print(f"Hello {guest.title()}! \nYou are invited to a dinner.\n")

#3-7
print("I can invite only 2 :(")
print(f"Hello {guests.pop().title()}! \nI'm sorry, but I can't invite you to a dinner.\n")
print(f"Hello {guests.pop().title()}! \nI'm sorry, but I can't invite you to a dinner.\n")
print(f"Hello {guests.pop().title()}! \nI'm sorry, but I can't invite you to a dinner.\n")
print(f"Hello {guests.pop().title()}! \nI'm sorry, but I can't invite you to a dinner.\n")
print(f"Hello {guests.pop().title()}! \nI'm sorry, but I can't invite you to a dinner.\n")
for guest in guests:
    print(f"Hello {guest.title()}! \nYou are invited to a dinner.\n")
del guests[0]
del guests[0]
print("--------")
print(guests)