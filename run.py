import random
from nltk.corpus import words
wordlist = words.words()

guillotine = [
    r"""

/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
    ||        ||
    ||        ||
    ||        ||
    ||        ||
----------------
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||________||
    ||        ||
    ||        ||
    ||        ||
----------------
/________________\-----------|
|                |-----------|
|                            |
|____________________________|
""",
    r"""
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||__@@@@__||
    || @|..|@ ||
    ||O@`=='@O||
    ||_@\/\/@_||
-----------------
/________________\-----------|
|                |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_
    ||--------||   |
    ||        ||   |
    ||        ||   |
    ||        ||   O
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||        ||
    ||__@@@@__||
    || @|..|@ ||
    ||O@`=='@O||
    ||_@\/\/@_||
-----------------
/________________\-----------|
|                |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_
    ||--------||   |
    ||        ||   |
    ||        ||   |
    ||        ||   O    __
    ||        ||   \\  (..)
    ||        ||    \\_|  |_
    ||        ||     \\ \/  )
    ||        ||      :    :|
    ||        ||      :    :|
    ||        ||      :====:O
    ||        ||      (    )
    ||__@@@@__||      | `' |
    || @|..|@ ||      | || |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|                |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_  _________
    ||--------||   |(You Lose!)
    ||-_      ||   | ---------
    ||   -_   ||   |    //
    ||      -_||   O    __
    ||        ||   \\  (..)
    ||        ||    \\_|  |_
    ||        ||     \\ \/  )
    ||        ||      :    :|
    ||        ||      :    :|
    ||        ||      :====:O
    ||        ||      (    )
    ||__@@@@__||      | `' |
    || @|..|@ ||      | || |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|                |-----------|
|                            |
|____________________________|
"""
]


def get_game_word():
    game_word = random.choice(wordlist)
    return game_word.upper()


def main():
    """
    Main that runs the game of Keep your head
    """
    print("Welcome to keep your head")
    incorrect_letters = []
    correct_letters = []

    while True:

        guess = player_guess()
        """player_guess will be function that gets the guess for the game"""

        if guess in get_game_word():
            correct_letters.append(guess)

    validate_username()


def player_guess():
    while True:
        print("Guess a letter")
        guess = input(" ").upper()
        if not guess.isalpha():
            print("Please enter a letter")
        else:
            return guess


def validate_username():
    """
    Validates the username to ensure that it contain only letter,
    so that numbers or whitespace can't be enter.
    """
    while True:
        username = input("Please enter you name:")
        print(username)
        if username.isalpha():
            break
        print("INVALID NAME, please try again")


main()
