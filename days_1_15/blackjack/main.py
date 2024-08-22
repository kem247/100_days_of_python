from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_total(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)

    return sum(deck)


def draw_ans():
    choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    return choice


def draw_compare(user, computer):
    if user == computer:
        return "Draw!"
    elif computer == 0:
        return "You lose, computer has Blackjack!"
    elif user == 0:
        return "You win, Blackjack!"
    elif user > 21:
        return "You lose, you went over!"
    elif computer > 21:
        return "You win, computer went over!"
    elif user > computer:
        return "You win!"
    else:
        "You lose!"


def add_to_deck():
    card = random.choice(cards)
    return card


def black_jack():
    print(logo)
    is_game_over = False

    user = random.sample(cards, 2)
    computer = random.sample(cards, 2)
    computer_score = -1
    user_score = -1
    while not is_game_over:
        user_score = add_total(user)
        computer_score = add_total(computer)
        print(f"Your cards: {user}, current score: {user_score} ")
        print(f"Computer's first card: {computer[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = draw_ans()
            if choice == 'y':
                user.append(add_to_deck())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer.append(add_to_deck())
        computer_score = add_total(computer)
    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer final hand: {computer}, final score: {computer_score}")
    print(draw_compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    black_jack()
