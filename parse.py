#!/usr/bin/env python3

# Set up a list to parse through

lunch = ["tacos","plantains","orange juice","wraps",["grape","apple","pear"]]

# A while loop is longwinded but will always work

current = 0
while current < len(lunch):
     print("Denise ate all the",lunch[current])
     current += 1

lunch[1] = "crumbs"
lunch.append("Bourbon");

# Using for to step through the indexes ...

for current in range(len(lunch)):
     print("Michelle missed out on the",lunch[current])

for current in (0,2,3,1):
     print("Keith also missed out on the",lunch[current])

     # Using for to step through the contents ...

for current in lunch:
     print("Trina was hankering after the",current)
