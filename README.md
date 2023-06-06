# Hangman-project documentation
This file provides a brief documentation on the steps undertaken for implementing the Hangman game. The Hangman game is a simple game where one user ("the host") chooses a word in their mind and the other user ('guesser) needs to guess the word within a finite number of chances. The guesser can guess letters comprising the word and the host needs to confirm whether or not that letter is part of the word.

## How to play the game
To play the game, initialise a `Hangman` class with within the `play_game` method, with input being a list of words for the guesser to guess from.

## Hangman class: Attributes
A Hangman class has been created with five attributes
- `num_lives`: Number of lives for user
- `word_list`: List of words the computer will randomly choose from
- `word`: Word chosen by computer from word_list 
- `word_guessed`: Includes the letters of the word guessed correctly by the user so far
- `num_letters` which is the number of unique leters in the word
- `list_of_guesses`:  Records all letter guesses made by user so far

## Hangman class: Methods
The Hangman class also has two methods. Both methods also update value of some attributes once run
- `ask_for_input`: This asks the user for input (their guess of the letter). It validates the input.
- `check_guess`: This checks whether the letter is part of the word

## Function to play the game
Finally, we have created a function called `play_game` to actually play the game with users. It incorporates the Hangman class and calls on the different Hangman instance methods.
All docstrings have been added to explain classes and methods in the file

## Concepts used in this game:
- Docstrings
- Classes
- Methods/functions
- Git/Github
- Abstraction (OOP)

