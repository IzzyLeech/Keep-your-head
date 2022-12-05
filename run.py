import random

import sys

import requests


e_words = ["ideas", "paris", "civil", "monks", "reign", "guild", "louis",
           "marat", "pope", "coup", "class", "jury", "cake", "vote",
           "lyon", "king", "elite", "state", "rebel", "trial", "royal", ]

m_words = ["liberal", "france", "terror", "regime", "peasant", "clergy",
           "estate", "rights", "society", "private", "nobility", "church",
           "bishop", "throne", "palace", "nature", "feudal", "culture",
           "general", "prison", ]

h_words = ["ideology", "liberty", "hercules", "elephant", "equality",
           "fraternity", "monarchy", "election", "robespierre",
           "rousseau", "governemnt", "democracy", "radical",
           "revolution", "napoleon", "jacobins", "girondins",
           "directory", "bastille", "freedom", ]


def get_easy_words():
    """
    Gets 10 random words that are 4 letter long from API
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10&length=4", timeout=10)

    easy_words = req.text

    return easy_words


def get_medium_words():
    """
    Gets 10 random words that are 6 letter long from API
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10&length=6", timeout=10)

    medium_words = req.text

    return medium_words


def get_hard_words():
    """
    Gets 10 random words that are 8 letter long from API
    """
    req = requests.get("https://random-word-api.herokuapp.com/word?number=10&length=8", timeout=10)

    hard_words = req.text

    return hard_words


def format_word(string):
    """
    Formats the API into a list, that removes "," "[" and "]"
    """
    current_word = ""
    new_list = []

    for letter in string:
        if letter.isalpha():
            current_word += letter
        elif letter == "," or letter == "]":
            new_list.append(current_word)
            current_word = ""

    return new_list


guillotine = [
    r"""
                    _________
                    (7 lives!)
                     --------
                        //
                        __
                       (..)
                      _|  |_
                     (\ \/  )
                     |:    :|
                     |:    :|
                     O:====:O
                      (    )
                      | `' |
                      | || |
                      | || |
                      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
                     _________
                    (6 lives!)
                     --------
                        //
                        __
                       (..)
                      _|  |_
                     (\ \/  )
                     |:    :|
                     |:    :|
                     O:====:O
                      (    )
      ________        | `' |
    ||        ||      | || |
    ||        ||      | || |
    ||________||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
                     _________
                    (5 lives!)
                     --------
                        //
                        __
                       (..)
                      _|  |_
                     (\ \/  )
                     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||        ||      (    )
    ||________||      | `' |
    ||        ||      | || |
    ||        ||      | || |
    ||________||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
                    _________
                    (4 lives!)
                     --------
                        //
                        __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||        ||      (    )
    ||________||      | `' |
    ||        ||      | || |
    ||        ||      | || |
    ||________||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_ _________
    ||--------||   |(3 lives!)
    ||        ||   | --------
    ||        ||   |    //
    ||        ||   O    __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||        ||      (    )
    ||________||      | `' |
    ||        ||      | || |
    ||        ||      | || |
    ||________||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_ _________
    ||--------||   |(2 lives!)
    ||        ||   | --------
    ||        ||   |    //
    ||        ||   O    __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||        ||      (    )
    ||__@@@@__||      | `' |
    || @|..|@ ||      | || |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
""",
    r"""
    _____________
    |____________|_  _________
    ||--------||   | (1 live!)
    ||        ||   | ---------
    ||        ||   |    //
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
|   GUILLOTINE   |-----------|
|                            |
|____________________________|
"""
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
    || @|xx|@ ||      | || |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
-----------------     '_'`_`
/________________\-----------|
|   GUILLOTINE   |-----------|
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
    """
    Input field for the player to choose the difficluty of word for game.
    """
    print("Pick a difficulty")
    print("E for easy, M for medium and H for hard")
    difficulty = input(" Please Enter Difficulty:")
    return difficulty.upper()


def validate_difficulty():
    """
    Validates the difficulty input for correct value
    """
    difficulty = get_difficulty()

    while difficulty not in ('E', 'M', 'H'):
        print('Please choose E, M or H')
        difficulty = get_difficulty()

    return difficulty


def get_difficulty_word():
    """
    Returns the word that will be played based on the difficulty
    that has been selected
    """
    difficulty = validate_difficulty()
    if difficulty == "H":
        words = format_word(get_hard_words())
        game_word = random.choice(words)
    elif difficulty == "M":
        words = format_word(get_medium_words())
        game_word = random.choice(words)
    elif difficulty == "E":
        words = format_word(get_easy_words())
        game_word = random.choice(words)

    print(game_word)
    return game_word.upper()


def game():
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
                print("You win " + username + " ,the word is:", game_word)
                play_again(username)
                break
        else:
            incorrect_letters.append(guess)
            if len(incorrect_letters) == len(guillotine) - 1:
                build_guillotine(incorrect_letters, correct_letters, game_word)
                print("You lose your head", username)
                print("The word was", game_word)
                play_again(username)
                break


def build_guillotine(incorrect_letters, correct_letters, game_word):
    lives = 7
    print(guillotine[len(incorrect_letters)])
    print()
    print("Incorrect letters:", end='')
    for letter in incorrect_letters:
        print(letter, end='')
        lives = lives - 1
    if len(incorrect_letters) == 0:
        print("No incorrect letters")
    print()
    empty_spaces = ["_"] * len(game_word)

    for i in range(len(game_word)):
        if game_word[i] in correct_letters:
            empty_spaces[i] = game_word[i]

    print("Number of lives:", lives)
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


def play_again(username):
    again = input("Would you like to play again" + username + "? Type Y or N")
    if again == "y":
        print("Let's go")
        game()
    else:
        print("No problem, Thanks for Playing")
        sys.exit()


def main():
    game()


print(r"""
█▄▀ █▀▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █░█ █▀▀ ▄▀█ █▀▄
█░█ ██▄ ██▄ █▀▀   ░█░ █▄█ █▄█ █▀▄   █▀█ ██▄ █▀█ █▄▀
""")
main()
