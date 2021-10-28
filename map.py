import random
# Creates a list of places the player can go
locations = ["Treasure room", "Combat room", "Rest room"]

# Creates a dictionary of places in the game
loc_text = {"Treasure room":
              {"text": "You see a small chest, open it and see whats inside"},
            "Hallways":
              {"text": "You enter the hallway and move forward through the dungeon"},
            "Combat room":
              {"text": "An enemy jumps out and attacks you"},
            "Rest room":
              {"text": "You enter a room where you can rest a and heal"},
            "Dragon room":
              {"text": "You approach the room where the dragon lives, prepare for the final battle"}}

print(f"You start out in the hallways knowing that at the end of it the dragon lays")
print(f"You have to loot the dungeon to stand a chance against the beast")
print(f"Good luck")

# Creates a counter to when the player will be placed in dragon room
room_past = 0

while room_past < 10:
    print(f"Would you like to enter ther room or keep moving forward in the hallway")
    print(f"Move or Enter")
    enter = input()
    if enter.lower() == "enter":
        play_location = random.choice(locations)
        """Prints text if player is in treasure room"""
        if play_location.lower() == "treasure room":
            roomtext = loc_text["Treasure room"]["text"]
            print(f"{roomtext}")
            room_past = room_past + 1
        """Prints text if player is in treasure room"""
        if play_location.lower() == "combat room":
            roomtext = loc_text["Combat room"]["text"]
            print(f"{roomtext}")
            room_past = room_past + 1
        """Prints text if player is in treasure room"""
        if play_location.lower() == "rest room":
            roomtext = loc_text["Rest room"]["text"]
            print(f"{roomtext}")
            room_past = room_past + 1
    """Creates a skip room option """
    if enter.lower() == "move":
        room_past = room_past + 1
    """Creates an invalid input statement"""
    if enter.lower not in ("move", "enter"):
        print("Please enter a valid input")

# Creates a system where after 10 rooms you face the dragon
if room_past == 10:
    loc_text = loc_text["Dragon room"]["text"]
    print(f"{loc_text}")
