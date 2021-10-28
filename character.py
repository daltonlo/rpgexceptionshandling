# imports the character inventories
from inventory import inventories

# Creates a list of character choices
characters = ["Wizard", "Knight", "Adventurer"]

# Prints out a list of possible character choices
for person in characters:
    print(f"Would you like to be a {person}")

# Creates a variable to keep track of the character choice
char_choice = input("")

# Creates a variable to check if the character select is finished
player_check = 0

while player_check == 0:
    try:
        """Prints inventory if character is the wizard"""
        if char_choice.lower() == "wizard":
            del inventories["Knight"]
            del inventories["Adventurer"]
            for character in inventories:
                for weapon in inventories[character]:
                    print(f"The {character} has a {weapon}")
                    for description in inventories[character][weapon]:
                        print(inventories[character][weapon][description])
                        player_check = 1
        """Prints inventory if character is the knight"""
        if char_choice.lower() == "knight":
            del inventories["Wizard"]
            del inventories["Adventurer"]
            for character in inventories:
                for weapon in inventories[character]:
                    print(f"The {character} has a {weapon}")
                    for description in inventories[character][weapon]:
                        print(inventories[character][weapon][description])
                        player_check = 1
        """Prints inventory if the character is a adventurer"""
        if char_choice.lower() == "adventurer":
            del inventories["Wizard"]
            del inventories["Knight"]
            for character in inventories:
                for weapon in inventories[character]:
                    print(f"The {character} has a {weapon}")
                    for description in inventories[character][weapon]:
                        print(inventories[character][weapon][description])
                        player_check = 1
        """Creates an exception if the player types an invalid character"""
        if char_choice.lower() not in ("wizard", "knight", "adventurer"):
            raise Exception("")
        """Handles exception created from invalid input"""
    except:
        print(f"Please enter Wizard Knight or Adventurer")
        char_choice = input("")
        pass
 