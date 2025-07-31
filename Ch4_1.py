magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

#4-1
pizzas = ['margerita', 'veggie', 'buffala']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I like pizzas.")

#4-2
animals = ['cat', 'dog', 'chicken']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("All this animals are cute.")
print("--------------------")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = list()
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

#4-3
for num in range(1, 21):
    print(num)

#4-4
# print("To the million:")
# for num in range(1, 1000001):
#     print(num)

#4-5
million_numbers = range(1, 1000001)
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#4-6
for num in range(1, 21, 2):
    print(num)

#4-7
for num in range(3, 31, 3):
    print(num)

#4-8
for num in range(1, 11):
    print(num**2)

#4-9
cubes = [num**2 for num in range(1, 11)]
print(cubes)