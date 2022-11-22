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
    word = random.choice(wordlist)
    print(word)
    return word.upper()


def main():
    # validate_username()
    """
    Main that runs the game of Keep your head
    """
    print("Welcome to keep your head")
    incorrect_letters = []
    correct_letters = []
    game_word = get_game_word()
    while True:

        guess = player_guess(incorrect_letters + correct_letters)
        """player_guess will be function that gets the guess for the game"""

        if guess in game_word:
            correct_letters.append(guess)
            word_corect = True
            for game_word_letter in game_word:
                if game_word_letter not in correct_letters:
                    word_corect = False
                    break
            if word_corect:
                print("You win, the word is:", game_word)
                break
        else:
            incorrect_letters.append(guess)
            if len(incorrect_letters) == len(guillotine):
                print("You lose your head")
                print("The word was", game_word)


def player_guess(repeat_guess):
    while True:
        print("Guess a letter")
        guess = input(" ").upper()
        if not guess.isalpha():
            print("Please enter a letter")
        elif len(guess) != 1:
            print("PLease enter one letter")
        elif guess in repeat_guess:
            print("You already have guessed that letter. Try again")
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


print(r"""
█▄▀ █▀▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █░█ █▀▀ ▄▀█ █▀▄
█░█ ██▄ ██▄ █▀▀   ░█░ █▄█ █▄█ █▀▄   █▀█ ██▄ █▀█ █▄▀
""")
main()
