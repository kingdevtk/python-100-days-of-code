#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# def calculate_tip (bill_total, desired_tip, number_of_people):

#     #calculate the total each person should pay excluding tip
#     each_person_subtotal = (bill_total) / (number_of_people)

#     #calculate the tip
#     tip = (desired_tip) / 100 + 1

#     #calculate total including tip
#     total = each_person_subtotal * tip

#     #format result to 2 decimal places
#     return round(total, 2)

# if __name__ == '__main__':
#     print('Welcome to the tip calculator!')

#     bill_total = input('What was the total bill? ')

#     desired_tip = input('How much tip would you like to give? 10, 12, or, 15? ')

#     number_of_people = input('How many people to split the bill? ')

#     result = calculate_tip (float(bill_total), float(desired_tip), float(number_of_people))

# print(result)

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
