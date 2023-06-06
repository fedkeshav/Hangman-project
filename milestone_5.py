
import random
class Hangman():
    '''
    This is a class containing five attributes and two methods, and is used for playing the Hangman game.

    The five attributes are
    1. Word_list = The list of words for computer to choose from
    2. Num_lives = The number of guesses the user still has. Default set to 5.
    3. Word = The word randomly chosen by the computer
    4. Num_letters = Number of unique letters in the word
    5. List of guesses = Letters guessed so far by the user

    The two methods are defined below
    '''
    def __init__(self, word_list: list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list        
        self.word = random.choice(word_list).lower()
        self.word_guessed =[]
        for i in range(len(self.word)):
            self.word_guessed.append('_')                          
        self.num_letters = len(list(set(self.word)))               
        self.list_of_guesses = []                               

    def check_guess(self, guess):
        '''
        Prints message of whether or not the letter is in the word. Changes num_letters and num_lives
        
        Args:
            guess = letter guessed by user

        '''
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! The letter {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters -= 1   
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry! The letter {guess} is not in the word')
            print(self.word_guessed)
            print(f'You have {self.num_lives} lives left')

    def ask_for_input(self):
        '''
        Asks user to pass through valid input, and then checks if the letter was already entered 
        before by looking at list_of_guesses attribute. If not, adds it to the attribute
        '''
        while True:
            guess = input('Enter a single letter: ')
            if guess.isalpha() == False and len(guess) != 1:
                guess = input('Invalid.Please enter a single alphabetical character: ')
            elif guess in self.list_of_guesses:
                print('You already tried that letter! ')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


# Defining a function that runs the game
def play_game(word_list):    
    '''
    Main method to play the game with the user

    Args:
        word_list: List of words for the guesser to guess from
    '''
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
            print(f'Word was {game.word}')
            print(f'You guessed so far {game.word_guessed}')
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_letters == 0:
            print('Congratulations. You won the game')
            print(f'Word was {game.word}')
            print(f'You guessed so far {game.word_guessed}')
            break

# Code to play the game
fruit_list = ['Apple', 'Bananas', 'Orange', 'Strawberry','Grapes']
play_game(fruit_list)
