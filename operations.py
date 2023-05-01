height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#calculate height
squared_height = float(height) ** 2
#calculate bmi
bmi = int(weight) // int(squared_height)

print(bmi)
