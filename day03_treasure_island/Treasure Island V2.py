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
*******************************************************************************''')

print("Hello Ember.... Welcome to MY Treasure Island")
print("")
print("You will be facing this same challenges as previously but, this time you won't be able to rely on your Hunches to power"
      "on through")
print("")
print("As the famous quote in Dark Souls... It's time for you to GIT GOOD")
print("Sincerely, Caelen")

direction = input("You are at a Crossroad. There are 3 options this time... Which way do you want to go? LEFT, RIGHT,... Or CENTER.\n".lower())

if direction.lower() == "right":
    river_path = input("You come to a river that you must pass. You see a Ferryman sitting on the dock across the river enjoying his break... It looks like it can take a while "
                       "before he decides to come over. You think the current is calm enough to swim across... What do you do? SWIM or WAIT\n".lower())
    if river_path == "wait":
        print("As you sit and wait for the ferryman to come over, you see an old fishing rod and some bait just sitting there..."
                        "You figure that the Ferryman must have forgotten his fishing gear and see no harm in fishing to pass the time")


        fishing_rod = input("You... CONTINUE WAITING or FISH\n")
        if fishing_rod == "continue waiting":

            castle_door = input("You decided to wait not knowing what the narrator has in store for you..."
                                "You waited for a few hours before the Ferryman finally notices you and crosses the river and takes you to the other side"
                                "you make it to the castle and notice 3 different doors. on the left hand you see a golden door, on the right hand you see a silver door, "
                                "and in the center its just a plain wooden door."
                                "you pick the... GOLD, SILVER, or WOOD\n")

            if castle_door == "wood".lower():
                print("You walk through the plain door... There's a chest inside full of gold."
                        "YOU WIN!")
            elif castle_door == "gold".lower():
                print("You make you way to the golden door only to be electrocuted after touching the handle")

            elif castle_door == "silver".lower():
                print("As you made your way to the silver door."
                      "You find Caelen waiting for you on the other side. ")


