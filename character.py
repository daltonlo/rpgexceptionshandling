# imports the character inventories
from inventory import inventories

# Creates a list of character choices
characters = ["Wizard", "Knight", "Adventurer"]

# Prints out a list of possible character choices
for person in characters:
    print(f"Would you like to be a {person}")

# Creates a variable to keep track of the character choice
char_choice = input("")

# Creates a invalid input statement
# Code addapted from stack Over flow
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while char_choice.lower() not in ("wizard", "knight", "adventurer"):
    print(f"Please enter a valid input")
    char_choice = input("")

# Creates a situation if character is the knight
if char_choice.lower() == "wizard":
    del inventories["Knight"]
    del inventories["Adventurer"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])

# Creates a situtaion if character is the knight
if char_choice.lower() == "knight":
    del inventories["Wizard"]
    del inventories["Adventurer"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])

# Creates a situation if the character is a adventurer
if char_choice.lower() == "adventurer":
    del inventories["Wizard"]
    del inventories["Knight"]
    for character in inventories:
        for weapon in inventories[character]:
            print(f"The {character} has a {weapon}")
            for description in inventories[character][weapon]:
                print(inventories[character][weapon][description])
                char_choice = "adventurer"
