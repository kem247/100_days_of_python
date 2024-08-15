from random import randint
from art import logo
EASY_LEVEL = 10
HARD_LEVEL = 5


def check(user_guess, random_number, turns):
    if user_guess > random_number:
        print(f"Too High.\n Guess again.\n You have {turns}"
              f" guesses left.")
        return turns - 1
    elif user_guess < random_number:
        if turns == 1:
            print(f"Too Low.\nGuess again.\nYou have {turns}"
                  f" guess left.")
        elif turns == 0:
            print(f"Too Low.\nYou have {turns}"
                  f" guesses left.")
        else:
            print(f"Too Low.\nGuess again.\nYou have {turns}"
                  f" guesses left.")
        return turns - 1
    else:
        print(f"Correct! You win! The answer was {random_number}")


def set_level_difficulty():
    level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(logo)
    print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    choice = set_level_difficulty()
    guess = 0
    random_number = randint(1, 100)
    while guess != random_number:
        guess = int(input("Make a guess: "))
        choice = check(guess, random_number, choice)
        if choice == -1:
            print(f"You've run out of guesses! The answer was {random_number}.")
            return
        elif guess != random_number and choice != -1:
            print("It's all good!")


game()
