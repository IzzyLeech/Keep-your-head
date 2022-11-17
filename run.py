import random
from nltk.corpus import words

wordlist = words.words()
random_word = random.choice(wordlist)


def main():
    validate_username()


def validate_username():
    while True:
        username = input("Please enter you name:")
        if username.isalpha():
            break
        print("INVALID NAME, please try again")


print("Welcome to keep your head")
main()
