# Creates a list of characters weapons
inventories = {"Wizard":
                {"Magic Wand":
                  {"description": "Uses magic to cast spells on enemies"}},
              "Knight":
                {"Sword":
                  {"description": "A metal weapon used for close range combat"},
                "Shield":
                  {"description": "Used to block or parry enemie attacks"}},
              "Adventurer":
                {"Map":
                  {"description": "A map of the dungeon"},
                "Dagger":
                  {"description": "A small blade with very minimal damage"}}}

# Prints out characters and dictionary
for character in inventories:
    print(f"The {character}:")
    for weapon in inventories[character]:
        for description in inventories[character][weapon]:
            play_text = inventories[character][weapon][description]
            print(f"  The {weapon} - {play_text}")
