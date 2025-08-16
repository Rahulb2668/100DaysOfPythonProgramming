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


user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
choices = [rock, paper, scissors]
winning_streaks = [1, 2, 0]

print("You choose", user_input)
print(choices[user_input])

computer_choice =random.randint(0,2)
print(choices[computer_choice])
print("Computer choose", computer_choice)

if user_input == computer_choice:
    print("Its a draw")
elif winning_streaks[user_input] == computer_choice:
    print("Computer wins")
else:
    print("You win")

