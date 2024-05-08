# ask user for name
name = input("What's your name? ")

# clean user input
name = name.strip().title()

# greet user
print(f"hello, {name}")