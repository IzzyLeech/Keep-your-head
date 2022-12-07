import random

import sys

import requests

from words import e_words

from words import m_words

from words import h_words


def get_easy_words():
    """
    Gets 10 random words that are 4 letter long from API
    """
    req = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=4",
        timeout=10)

    easy_words = req.text

    return easy_words


def get_medium_words():
    """
    Gets 10 random words that are 6 letter long from API
    """
    req = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=6",
        timeout=10)

    medium_words = req.text

    return medium_words


def get_hard_words():
    """
    Gets 10 random words that are 8 letter long from API
    """
    req = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=8",
        timeout=10)

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
                      |_||_|
/________________\|   '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
                     _________
                    (6 lives!)
                     --------
                        __
                       (..)
                      _|  |_
                     (\ \/  )
                     |:    :|
                     |:    :|
                     O:====:O
      ________        (    )
    ||        ||      | `' |
    ||        ||      | || |
    ||________||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
                     _________
                    (5 lives!)
                     --------
                        __
                       (..)
                      _|  |_
                     (\ \/  )
                     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||________||      (    )
    ||        ||      | `' |
    ||        ||      | || |
    ||________||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
                    _________
                    (4 lives!)
                     --------
                        __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||________||      (    )
    ||        ||      | `' |
    ||        ||      | || |
    ||________||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
    _______________ ________
    ||--------||   |(3 lives!)
    ||        ||   | --------
    ||        ||   O    __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||________||      (    )
    ||        ||      | `' |
    ||        ||      | || |
    ||________||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
    _______________ __________
    ||--------||   |(2 lives!)
    ||        ||   | --------
    ||        ||   O    __
    ||        ||       (..)
    ||        ||      _|  |_
    ||        ||     (\ \/  )
    ||        ||     |:    :|
    ||        ||     |:    :|
    ||        ||     O:====:O
    ||__@@@@__||      (    )
    || @|..|@ ||      | `' |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
    _______________ __________
    ||--------||   | (1 live!)
    ||        ||   | ---------
    ||        ||   O    __
    ||        ||   \\  (..)
    ||        ||    \\_|  |_
    ||        ||     \\ \/  )
    ||        ||      :    :|
    ||        ||      :    :|
    ||        ||      :====:O
    ||__@@@@__||      (    )
    || @|..|@ ||      | `' |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
|____________________________|
""",
    r"""
    _______________ __________
    ||--------||   |(You Lose!)
    ||-__     ||   | ---------
    ||   ---__||   O    __
    ||        ||   \\  (..)
    ||        ||    \\_|  |_
    ||        ||     \\ \/  )
    ||        ||      :    :|
    ||        ||      :    :|
    ||        ||      :====:O
    ||__@@@@__||      (    )
    || @|xx|@ ||      | `' |
    ||O@`=='@O||      | || |
    ||_@\/\/@_||      |_||_|
/________________\    '_'`_`
|   GUILLOTINE   |-----------|
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
    return username.upper()


def get_difficulty(username):
    """
    Input field for the player to choose the difficluty of word for game.
    """
    print("PLease pick a difficulty", username)
    print("E for easy, M for medium and H for hard")
    difficulty = input(" Please Enter Difficulty:")
    return difficulty.upper()


def validate_difficulty(username):
    """
    Validates the difficulty input for correct value
    """
    difficulty = get_difficulty(username)

    while difficulty not in ('E', 'M', 'H'):
        print('Please choose E, M or H', username)
        difficulty = get_difficulty(username)

    return difficulty


def get_difficulty_word_api(username):
    """
    Returns the word that will be played based on the difficulty
    that has been selected from the API
    """
    difficulty = validate_difficulty(username)
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


def get_difficulty_word_py(username):
    """
    Returns the word that will be played based on the difficulty
    that has been selected from the words.py file
    """
    difficulty = validate_difficulty(username)
    if difficulty == "H":
        game_word = random.choice(h_words)
    elif difficulty == "M":
        game_word = random.choice(m_words)
    elif difficulty == "E":
        game_word = random.choice(e_words)

    print(game_word)
    return game_word.upper()


def check_if_api_is_active(username):
    """
    Check if the API is active by checking error
    code, if the api is down it will run words from the
    words.py file
    """
    req_easy = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=4",
        timeout=10)

    req_medium = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=6",
        timeout=10)

    req_hard = requests.get(
        "https://random-word-api.herokuapp.com/word?number=10&length=8",
        timeout=10)

    if req_easy.status_code == 503:
        game_word = get_difficulty_word_py(username)
        if req_medium.status_code == 503:
            game_word = get_difficulty_word_py(username)
            if req_hard.status_code == 503:
                game_word = get_difficulty_word_py(username)
    else:
        game_word = get_difficulty_word_api(username)
    return game_word


def game():
    """
    Main that runs the game of Keep your head
    """
    username = validate_username()
    print("Welcome to Keep Your Head,", username)
    print("A guessing game where you must find the letter's of a word")
    print("Or you will lose your head if you guess wrong 7 times")
    incorrect_letters = []
    correct_letters = []
    game_word = check_if_api_is_active(username)
    while True:
        build_guillotine(incorrect_letters, correct_letters, game_word)
        guess = player_guess(incorrect_letters + correct_letters, username)
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
    """
    Will print the different parts of the guillotine for incorrect guess,
    will print the incorrect letters, will print the empty spaces of the word,
    will print the correct guess in the empty spaces and will decrease the
    lives counter for incorrect guesses.
    """
    lives = 7
    print(guillotine[len(incorrect_letters)])
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


def player_guess(repeat_guess, username):
    """
    Will allow the user to input the guess for the game word
    Will make sure that one guess has been entered, no repeat guess and
    invalid guesses, then will return the guess.
    """
    while True:
        print("Guess a letter", username)
        guess = input("> ").upper()
        if not guess.isalpha():
            print("Please enter a letter", username)
        elif len(guess) != 1:
            print("PLease enter one letter", username)
        elif guess in repeat_guess:
            print("You already have guessed that letter. Try again")
        else:
            return guess


def play_again(username):
    """
    Gives the user the option to play the game again or
    close the program
    """
    again = input(
        "Would you like to play again " + username +
        "? Type Y, play again or N to close program").upper()
    while again not in ("Y", "N"):
        print("PLease choose y or n", username)
        again = input(
            "Would you like to play again " + username +
            "? Type Y to play again or N to close program")

    if again == "Y":
        print("Let's go")
        game()
    else:
        print("No problem, Thanks for Playing ", username)
        sys.exit()


def main():
    """
    Main function that runs the program
    """
    game()


print(r"""
                █▄▀ █▀▀ █▀▀ █▀█   █▄█ █▀█ █░█ █▀█   █░█ █▀▀ ▄▀█ █▀▄
                █░█ ██▄ ██▄ █▀▀   ░█░ █▄█ █▄█ █▀▄   █▀█ ██▄ █▀█ █▄▀
""")
main()
