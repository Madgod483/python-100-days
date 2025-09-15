import sys
import random
# Rock
Rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

# Paper
Paper = ('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')

# Scissors
Scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game_images = [Rock, Paper, Scissors]
random.choice(game_images)

user_choice = int(input("You are playing Rock, Paper, Scissors type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Invalid input, you typed in the wrong number... you lose")
    sys.exit()

print(f"You chose: {game_images[user_choice]}")
print(f"Computer chose: {game_images[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
    sys.exit()
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
    sys.exit()
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
    sys.exit()
elif user_choice < computer_choice:
    print("You lose!")
    sys.exit()
elif user_choice > computer_choice:
    print("You win!")
    sys.exit()

