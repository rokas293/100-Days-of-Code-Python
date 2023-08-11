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

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computers_choice = random.randint(0, 2)

if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
else:
    print(scissors)

print(f"Computer Chose: {computers_choice}")

if computers_choice == 0:
    print(rock)
elif computers_choice == 1:
    print(paper)
else:
    print(scissors)


if my_choice >= 3 or my_choice < 0:
    print("You've entered an invalid number, You Lose!")
if computers_choice == 0 and my_choice == 2:
    print("You Lose!, Rock wins against Scissors")
elif computers_choice == 0 and my_choice == 1:
    print("You Win!, Paper wins against Rock")
elif computers_choice == 1 and my_choice == 0:
    print("You Lose!, Paper wins against Rock")
elif computers_choice == 1 and my_choice == 2:
    print("You Win!, Scissors wins against Paper")
elif computers_choice == 2 and my_choice == 0:
    print("You Win!, Rock wins against Scissors")
elif computers_choice == 2 and my_choice == 1:
    print("You Lose!, Scissors wins against Paper")
else:
    print("It's a draw")
