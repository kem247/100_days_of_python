import random
from art import logo
from art import vs
from game_data import data


def list_a_and_b(choice):
    return f'{choice["name"]}, a {choice["description"]} from {choice["country"]}.'


# if A has more followers and they guessed A, then return true if B has
#
# more followers and they guest B then return true, and if the opposite happens, then return false.
def check_answer(a_followers, b_followers):
    if a_followers > b_followers:
        return 'a'
    else:
        return 'b'


print(logo)
count = 0
choice_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    choice_a = choice_b
    choice_b = random.choice(data)
    if choice_a == choice_b:
        choice_b = random.choice(data)

    print(f"Compare A: {list_a_and_b(choice_a)}")
    print(vs)
    print(f"Against B: {list_a_and_b(choice_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n" * 20)
    print(logo)

    choice_a_followers = choice_a["follower_count"]
    choice_b_followers = choice_b["follower_count"]

    correct = check_answer(choice_a_followers, choice_b_followers)

    if correct:
        count += 1
        print(f"Correct! Your score is: {count}")
    else:
        print(f"Sorry that's wrong. Final Score: {count}")
        game_should_continue = False
