from milestone_2 import word_list
import random
import typing

# Computer chooses a random word from list of favourite fruits
random_word = random.choice(word_list)

# Creating functions for asking inputs and checking guesses:
def ask_for_input():
    guess = input('Enter the first letter of the Guess: ')
    while True:
        if guess.isalpha() and len(guess)==1 :
            break
        else:
            guess = input('Invalid.Please enter a single alphabetical character: ')

    check_guess(guess)


def check_guess(guess: str):
    guess = guess.lower()
    if guess in random_word:
        print(f'Good guess! The letter {guess} is in the word')
    else:
        print(f'Sorry! The letter {guess} is not in the word')


ask_for_input()
