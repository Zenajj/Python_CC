#2-3
name = "janez koncilija"
message = f"Hello {name.title()}! \n\tWould you like to learn some Python today?"
print(message)
#2-4
print(name.lower())
print(name.upper())
print(name.title())
#2-5
name = "alber einstein"
quote = "A person who never made a mistake nevertried anything new."
print(f"{name.title()} once said, '{quote}'")
#2-7
name = " Hinko sMREkar "
print(name.title())
print(name.lstrip().title())
print(name.lstrip().rstrip().title())
#2-8
file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))