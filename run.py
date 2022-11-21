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


def main():
    """
    Main that runs all function
    """
    validate_username()


def validate_username():
    """
    Validates the username to ensure that it contain only letter,
    so that numbers or whitespace can't be enter.
    """
    while True:
        username = input("Please enter you name:")
        if username.isalpha():
            break
        print("INVALID NAME, please try again")


def get_game_word():
    random_word = random.choice(wordlist)
    while ' ' in random_word:
        random_word = random.choice(wordlist)

    return random_word


print("Welcome to keep your head")
main()
