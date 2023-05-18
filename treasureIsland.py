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

subway = input('You\'re in the subway. Where do you want to go? Type "Brooklyn" or "Harlem". ')

if subway == 'Brooklyn':
    swim = input('You\'re in Coney Island, and there\'s a beach. Type "swim" to swim in the ocean. Type "rollercoaster" to ride the rollercoaster. ')

    if swim == 'swim':
        drink = input('You see your friend at the beach, and they invite you for drinks at a bar. Type "bourbon" or "tequila". ')
        if drink == 'burbon':
            print('You win!')
        elif drink == 'tequila':
            print('You choked on the worm. Game Over.')
        else:
            print('Game Over.')
    elif swim == 'rollercoaster':
        print('Coney Island is closed. Game over.')
    else:
        print('Coney Island is closed. Game Over.')

elif subway == 'Harlem':
    print('The train is not running today, game over.')
else:
    print('The train is not running today, game over.')
















