from art import logo
import random
import os

def guess_the_number():
    guess_this = random.randint(1, 100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # print(f"The correct answer is {guess_this}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5
    
    while guesses > 0:
        if guesses > 1:
            print(f"You have {guesses} remaining to guess the number.")
        else:
            print(f"Last try to guess the number that I'm thinking of.")
        attempt = int(input("Make a guess: "))
        if attempt < guess_this:
            print("Too Low!")
            if guesses > 1:
                print("Guess Again!")
        elif attempt > guess_this:
            print("Too high!")
            if guesses > 1:
                print("Guess Again!")
        elif attempt == guess_this:
            def game_over():
                print(f"Correct! The answer was {guess_this}. Thanks for completing that! 😁")
                return guesses - guesses
            guesses = game_over()
        elif guesses == 1:
            print("Game Over!")
            print(f"Unlucky! The correct answer was {guess_this}")
        guesses -= 1

    play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit.")
    if play_again == 'y':
        os.system('cls||clear')
        guess_the_number()
    else:
        print("Goodbye.")

guess_the_number()
