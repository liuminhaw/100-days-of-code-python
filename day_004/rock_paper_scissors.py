
import random

ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def main():
    """
    Rock paper scissors game
    """
    options = [ROCK, PAPER, SCISSORS]

    your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
    computer_choice = random.randint(0, 2)

    if your_choice > 2 or your_choice < 0:
        print('invalid input')
        return 0

    print(options[your_choice])

    print('Computer choice:')
    print(options[computer_choice])

    if your_choice == computer_choice:
        print("It's a draw")
    elif (your_choice == 1 and computer_choice == 0) or (your_choice == 2 and computer_choice ==1) or \
        (your_choice == 0 and computer_choice == 2):
        print('You win')
    else:
        print('You lose')

if __name__ == '__main__':
    main()
    