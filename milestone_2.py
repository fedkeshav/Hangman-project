import random
import string

word_list = ['Apple', 'Bananas', 'Orange', 'Strawberry','Grapes']
guess = input('Guess the first letter: ')

# Validating if user entered single character

if (len(guess)==1 and guess in string.ascii_letters): 
    print('Good guess')
else:
    print('Oops! That is not a valid input')

