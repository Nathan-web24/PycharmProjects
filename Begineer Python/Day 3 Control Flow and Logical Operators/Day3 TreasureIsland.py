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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to fine a treasure.")

choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'left'\n").lower()
if choice1 == "left":
    choice2 = input("You come to the lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
     choice3 = input("You arrived at island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n").lower()
     if choice3 == "yellow":
      print("You've found the treasure. You win the game.")
     elif choice3 == "red":
      print("It's a room full of fire. Game Over.")
     elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
     else:
      print("You choose the door that doesn't exist. Game Over.")
    else:
     print("You are attacked by trout. Game Over.")
else:
 print("You've fall into the hole. Game Over")




