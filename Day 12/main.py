import random

from art import logo

EASY_MODE_GUESSES =10
HARD_MODE_GUESSES = 5

def set_game_tries (mode):
    return EASY_MODE_GUESSES if mode == "easy" else HARD_MODE_GUESSES


def compare_guesses (c_guess,u_guess, tries_left):
    if c_guess == u_guess:
        print(f"You got it right guessed number is {c_guess}")
        return True, tries_left
    elif c_guess >u_guess:
        print("Guessed Too Low")
    else:
        print("Guessed to High")

    return False, tries_left-1


def play_game():
    print(logo)
    print("Welcome to the Guessing Game")
    game_mode = input("Choose your game mode 'easy' or 'hard'")
    tries_left = set_game_tries(game_mode)
    computer_guess = random.randint(1, 100)
    # print(computer_guess)

    while tries_left > 0:
        user_guess = int(input("Guess the number"))
        won, tries_left = compare_guesses(computer_guess, user_guess, tries_left)

        if won:
            return

    print(f"Game Over Computer Guess was {computer_guess}")


play_game()