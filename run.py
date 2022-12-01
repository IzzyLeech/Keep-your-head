import random

easy_words = ["ideas", "paris", "civil", "monks", "reign", "guild", "louis", "marat", "pope", "coup", "class", "jury", "cake", "vote", "lyon", "king", "elite", "state", "rebel", "trial", "royal", ]

medium_words = ["liberal", "france", "terror", "regime", "peasant", "clergy", "estate", "rights", "society", "private", "nobility", "church", "bishop", "throne", "palace", "nature", "feudal", "culture", "general", "prison", ]

hard_words = ["ideology", "liberty", "hercules", "elephant", "equality", "fraternity", "monarchy", "election", "robespierre", "rousseau", "governemnt", "democracy", "radical", "revolution", "napoleon", "jacobins", "girondins", "directory", "bastille", "freedom", ]

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
    return username


def get_difficulty():
    print("Pick a difficulty")
    print("E for easy, M for medium and H for hard")
    difficulty = input(" Please Enter Difficulty:")
    return difficulty.upper()


def validate_difficulty():
    difficulty = get_difficulty()

    while difficulty not in ('E', 'M', 'H'):
        print('Please choose E, M or H')
        difficulty = get_difficulty()

    return difficulty


def get_difficulty_word():
    difficulty = validate_difficulty()
    if difficulty == "H":
        game_word = random.choice(hard_words)
    elif difficulty == "M":
        game_word = random.choice(medium_words)
    elif difficulty == "E":
        game_word = random.choice(easy_words)
    print(game_word)
    return game_word.upper()


def main():
    """
    Main that runs the game of Keep your head
    """
    username = validate_username()
    print("Welcome to keep your head,", username)
    incorrect_letters = []
    correct_letters = []
    game_word = get_difficulty_word()
    while True:
        build_guillotine(incorrect_letters, correct_letters, game_word)
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
            if len(incorrect_letters) == len(guillotine) - 1:
                build_guillotine(incorrect_letters, correct_letters, game_word)
                print("You lose your head")
                print("The word was", game_word)
                break


def build_guillotine(incorrect_letters, correct_letters, game_word):
    print(guillotine[len(incorrect_letters)])
    print()
    print("Incorrect letters:", end='')
    for letter in incorrect_letters:
        print(letter, end='')
    if len(incorrect_letters) == 0:
        print("No incorrect letters")
    print()
    empty_spaces = ["_"] * len(game_word)

    for i in range(len(game_word)):
        if game_word[i] in correct_letters:
            empty_spaces[i] = game_word[i]

    print("".join(empty_spaces))


def player_guess(repeat_guess):
    while True:
        print("Guess a letter")
        guess = input("> ").upper()
        if not guess.isalpha():
            print("Please enter a letter")
        elif len(guess) != 1:
            print("PLease enter one letter")
        elif guess in repeat_guess:
            print("You already have guessed that letter. Try again")
        else:
            return guess


print(r"""
█▄▀ █▀▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █░█ █▀▀ ▄▀█ █▀▄
█░█ ██▄ ██▄ █▀▀   ░█░ █▄█ █▄█ █▀▄   █▀█ ██▄ █▀█ █▄▀
""")
main()
