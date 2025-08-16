import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(deck):

    score = sum(deck)
    ace_count = deck.count(11)

    if score == 21 and len(deck) == 2:
        return 0

    if ace_count > 0 and score>21:
        score-=10

    return score

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose"
    elif u_score == 0:
        return "Win"
    elif u_score > 21:
        return "Lose"
    elif c_score > 21:
        return "you win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose 😤"

def play_blackjack():
    user_cards = [deal_cards(), deal_cards()]
    computer_cards = [deal_cards(),deal_cards()]
    computer_score = -1
    user_score = -1

    is_game_over = False



    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("Your deck", user_cards, "Total score", user_score)
        print("Computers deck", computer_cards[0])


        if user_score ==0 or computer_score == 0 or user_score>21:
            is_game_over = True
        else:
            another_draw = input("Would you like to do another draw 'y' or 'n'").lower()
            if another_draw == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 or computer_score< 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))




while True:
    play_game = input("Would you like to play game 'y' or 'n'").lower()
    if play_game == "y":
        play_blackjack()
