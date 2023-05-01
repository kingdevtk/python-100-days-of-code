# score = 0
# height = 1.8
# isWinning = True
# #f-String is used so you don't have to convert the different data types
# print(f'your score is {score}, your height is {height}, you are winning is {isWinning}')

age = input("What is your current age? ")
#calculate years
n = 90 - int(age)
#calculate days
x = int(age) * 365
#calculate weeks
y = int(age) * 52
#calculate months
z = int(age) * 12
#calculate days/weeks/months you have left
print(f'You have {x} days, {y} weeks, and {z} months left.')
