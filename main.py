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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
 
    
''')




print("Welcome to Treasure Island Escape!")
print("A game where the mission is to find the treasure and to stay alive!\n Let's begin...")
decision1 = input('You came to a cross road. Which way you want to go. Type "left" or "right" ').lower()

if decision1 == "left":
    decision2 = input('"You reached a lake and now you can either swim across or wait for a boat. \nType "swim" or "wait" ').lower()
    if decision2 == "wait":
        decision3 = input("The boat picked you up and you are now at the island and see 3 homes with different color doors." 
                          "\nType red, green, or blue ").lower()
        if decision3 == "red":
            print("The home is filled with lava. You did not make it. Game Over.")
        elif decision3 == "green":
            decision4 =input('"You see two treasure chests, one with a bell on top and the other one with a coin on top. Choose wisely. \nType "bell" or "coin" ').lower()
            if decision4 == "bell":
                print("You lost the game. The chest was empty and you were attacked by the beast.")
            else:
                print("You won the game! Your chest had the sword and you were able to defeat the beast of the island!")
        elif decision3 == "blue":
            print("The room is filled with water and you drowned. Game Over.")
        else: 
            print("You chose a door that does not exist. Game Over. ")
    else:
        print("You jumped into the lake with a pool of sharks. Game over. ")     

else:
    print("You were attacked by the beast. Game over.left")

 