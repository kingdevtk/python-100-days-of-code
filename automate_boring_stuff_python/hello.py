# This program says hello and asks for my name

print('Hello world!')

print('what is your name?') # ask for their name
myName = input()
print('nice to meet you, ' + myName)
print('the length of your name is:')
print(len(myName))

print('what is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')
