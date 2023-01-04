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



choice1 = input('You\'ve come to crossroad. Where do you want to go? Type "left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("A boat comes by and picks you up and takes you to the island. On the Island, there are three homes. A red home, a green home, and a blue home. Which do you want to enter?\n").lower()
    if choice3 == "red":
      print("You enter the red home, where a dark sith lord lives. It is VADER!!!. You get your head sliced off by his dark crimson red saber... GAME OVER!")
    elif choice3 == "green":
      print("You enter the green home, where a mandalorian stands 10 feet away from you. There is a small being next to him that removes its hood, and looks like Yoda. It is GROGU!!! YOU HAVE FOUND THE TREASURE!!!")
    elif choice3 == "blue":
      print("You enter the blue room, where a hooded figure stands 10 feet from you. It turns and faces you. It is Anakin Skywalker, who had just slayed a bunch of children in Order 66. He kills you. GAME OVER.")
    else:
      print("You fell into a black hole... GAME OVER!")
  else:
    print("You got attacked by sharks... GAME OVER!")
else:
  print("You run into the jungle, where a jaguar leaps from a tree and mawls you.... GAME OVER!")