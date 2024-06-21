print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
name = input("What is your name treasure hunter? ")
print(f"{name} is standing in front of a cave")
direction1 = input(f"Does {name} want to go left or right? ")
if direction1.lower() == "left":
    lake = input(f"{name} has come to a lake. Does {name} want to swim across or wait? ")
    if lake.lower() == "wait":
        door = input(f"{name} was picked up by a friendly goblin and ferried across and has come to the final door. \nDoes {name} want to enter the blue, yellow, or purple door? ")
        if door.lower() == "blue":
            print(f"Congrats {name}! You have found the treasure. Be sure to share.")
        elif door.lower() == "yellow":
            print(f"Oh no! {name} was eaten by a troll!")
        else:
            print(f"The door shut behind you and {name} will starve to death.")
    else:
        print(f"The water was infested with sharks and {name} was eaten alive.")
else:
    print(f"Sorry {name}, you fell into a hole and died.")