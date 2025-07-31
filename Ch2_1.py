message = "Hello"
print(message)
message = "Hello 'python'!"
print(message)
message = 'Hello ""python"!'
print(message)

name = "jANez KoncilijA"
print(name.title())
print(name.lower())
print(name.upper())

#put variables in strings: f"{var} blah, blah"
first_name = "janez"
last_name = "koncilija"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
print(f"\tHello! \n{full_name.title()}!\nNice to see you!")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#remove whitespace: string.rstrip(), string.lstrip(), string.strip()
favourite_language = "python "
print(f"{favourite_language.rstrip()}!")

#remove prefix string.removeprefix("prefix")
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))