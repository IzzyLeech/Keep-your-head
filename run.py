import random
from nltk.corpus import words
wordlist = words.words()
random_word = random.choice(wordlist)


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


print("Welcome to keep your head")
main()
