import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# choice = input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ')


# user_choice = int(choice)
# computer_choice = random.randint(0, 2)

# if user_choice == computer_choice:
#     print('It is a draw, no one wins.')
# elif computer_choice == 0 and user_choice == 1:
#     print('Paper beats Rock, you win!')
# elif computer_choice == 1 and user_choice == 2:
#     print('Scissors beats Paper, you win!')
# elif computer_choice == 2 and user_choice == 0:
#     print('Rock beats Scissors, you win!')
# elif user_choice == 0 and computer_choice == 1:
#     print('Paper beats Rock, you lose.')
# elif user_choice == 1 and computer_choice == 2:
#     print('Scissors beats Paper, you lose.')
# elif user_choice == 2 and computer_choice == 0:
#     print('Rock beats Scissors, you lose.')

# else:
#     print('Thanks for playing!')


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
