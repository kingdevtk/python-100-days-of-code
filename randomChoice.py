import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

person_paying = random.choice(names)

print( person_paying + ' is going to buy the meal today!')
