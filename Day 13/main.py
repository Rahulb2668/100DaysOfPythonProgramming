# import random
#
# from art import logo, vs
# from game_data import data
# """
# 1. Make the user start game
# 2. Choose selection 1 and selection 2
# 3. Ask users input
# 4. If true make selection 2 to 1 and choose another 2
# 5. Increment correct answer count
# 6. repeat 3to 5 until wrong answer
# """
#
#
# def randomselection(option):
#     new_option = random.choice(data)
#     if new_option == option:
#         return randomselection(option)
#     else:
#         return new_option
#
#
#
# def format_data(option):
#     return f"{option["name"]}, a {option["description"]}, from {option["country"]}"
#
# def compare_guess(guess, option1, option2, current_score):
#     if guess == "a":
#         if option1["follower_count"] > option2["follower_count"]:
#             return True, current_score + 1, option1
#         else:
#             return False, current_score, option2
#     else:
#         if option2["follower_count"] > option1["follower_count"]:
#             return True, current_score + 1, option2
#         else:
#             return False, current_score, option1
#
#
# print(logo)
#
# game_start = True
# score = 0
# while game_start:
#     option1 = random.choice(data)
#     option2 = randomselection(option1)
#
#     correct_answer = True
#
#     while correct_answer:
#         print(f"Current Score: {score}")
#         print(f"Compare A : {format_data(option1)}")
#         print(vs)
#         print(f"Compare B: {format_data(option2)}")
#
#         guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#         correct_answer, score ,correct_option = compare_guess(guess, option1, option2, score)
#
#         if correct_answer:
#             option1 = correct_option
#             option2 = randomselection(option1)
#
#     game_start = False
#
# print("Final Score", score)


from art import logo, vs
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0

game_continue = True

account_b = random.choice(data)


while game_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False

