import random
from nltk.corpus import words

wordlist = words.words()
random_word = random.choice(wordlist)

print("Welcome to keep your head")
username = input("Please enter you name:")
print(username)
