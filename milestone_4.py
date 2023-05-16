import random

class Hangman():
    def __init__(self, word_list: list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed =[]
        for i in range(len(self.word)):
            self.word_guessed.append('_')                                     #  A list of the letters of the word, with for each letter not yet guessed
        print(self.word_guessed)
        self.num_letters = len(list(set(self.word)))               # The number of UNIQUE letters in the word that have not been guessed yet.
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []                                  # A list of the guesses that have already been tried

    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! The letter {guess} is in the word')
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters -= 1
            

        else:
            self.num_lives -= 1
            print(f'Sorry! The letter {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')



    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if guess.isalpha() == False:
                guess = input('Invalid.Please enter a single alphabetical character: ')
            elif guess in self.list_of_guesses:
                print('You already tried that letter! ')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

word_list = ['Apple', 'Bananas', 'Orange', 'Strawberry','Grapes']
hang = Hangman(word_list)
hang.ask_for_input()