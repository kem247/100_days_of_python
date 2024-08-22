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

#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) 

computer_choice = random.randint(0,2)
if user_choice == 0:
    print("You chose Rock")
    print(rock)
elif user_choice == 1:
    print("You chose Paper")
    print(paper)
elif user_choice == 2:
    print("You chose Scissors")
    print(scissors)
else:
    print("You chose an invalid number")

if computer_choice == 0:
    print("Computer chose Rock")
    print(rock)
elif computer_choice == 1:
    print("Computer chose Paper")
    print(paper)
else:
    print("Computer chose Scissors")
    print(scissors)
if computer_choice == 0 and user_choice == 1:
    print("You win")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == 1 and user_choice == 0:
    print("You lose")
elif computer_choice == 1 and user_choice == 2:
    print("You win")
elif computer_choice == 2 and user_choice == 0:
    print("You win")
elif computer_choice == 2 and user_choice == 1:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")
else:
    print("You chose an invalid number")