print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
c1=int(input("Choose left(1) or right(2):"))
if c1==1:
    print("We are walking towards a magical jungle")
    print("You see a cave between the trees.")
    c2=int(input("Choose 1 to get into the cave or 2 to explore the rest of the jungle: "))
    if c2==1:
        print(" hehehehhe, the rock has crushed you !! the game has ended ,try another path")
    else:
        print("you see a weird looking racoon walking on two feet!!")
        c3=int(input("choose 1 to talk to racoon , 2 to move on without talking to it:"))
        if c3==1:
            print("hello, are you here to find the treasure? If yes then find a huge tree with unusual flowers ")
            print("you keep exploring the forest and find a huge waterfall")
            print("it seems very sus at the beginning and then find a beam of light flashing through the waterfall.")
            c5=int(input("Choose 1 to get in and 2 to not:"))
            if c5==1:
                print("Congrats! You found the treasure using your amazing wits. Hurray!! Bravo!!")

            else:
                print("The waterfall rose beyond your eye level and you vanished :( Try again")
        else:
            print("You see two doors. Which one do you want open ?")
            c4=int(input("choose 1 to open a flowery door or 2 to open a fiery door:"))
            if c4==1 or 2:
                print("hehehehhe you just fell into the trap")



else:
    print(" hehehehehee, You got bit by a snake :( better luck next time ")
