import random
from nltk.corpus import words

wordlist = words.words()
random_word = random.choice(wordlist)
print(random_word)
