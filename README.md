# Hangman-project documentation
This file provides a brief documentation on the steps undertaken for implementing the Hangman game. The Hangman game is a simple game where one user ("the host") chooses a word in their mind and the other user ('guesser) needs to guess the word within a finite number of chances. The guesser can guess letters comprising the word and the host needs to confirm whether or not that letter is part of the word.

A Hangman class has been created with five attributes
- number of lives for user
- word list for computer to randomly choose from
- actual word chosen by computer 
- word guessed which includes the letters of the word guessed correctly by the user so far
- num_letters which is the number of unique leters in the word
- list_of_guesses which records all letter guesses made by user so far

The Hangman class also has two methods. Both methods also update value of some attributes once run
- ask_for_input: this asks the user for input (their guess of the letter). It validates the input.
- check_guess: this checks whether the letter is part of the word

Finally, we have created a function called play_game to actually play the game with users. It incorporates the Hangman class and calls on the different Hangman instance methods.
All docstrings have been added to explain classes and methods in the file

Concepts used in this game:
- Docstrings
- Classes
- Methods/functions
- Git/Github
- Abstraction (OOP)

Concepts not used in this game:
- static methods, decorators, class methods
- encapsulation
