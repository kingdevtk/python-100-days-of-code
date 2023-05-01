#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome to the tip calculator!')
# total bill amount
bill_total = input('What was the total bill? ')
# tip amount the user wants to give
desired_tip = input('How much tip would you like to give? 10, 12, or, 15? ')
# number of people that are splitting the bill
number_of_people = input('How many people to split the bill? ')
#calculate the total each person should pay
each_person_total = ((float(bill_total) / int(number_of_people) * ((float(desired_tip) / 100))))
#format result to 2 decimal places
print(round(each_person_total, 2))
