from string import digits, punctuation
from itertools import permutations

with open('dictionary.txt') as f:  # Open the dict file and add the words to a list
    dictionary = f.read().split()

punc = list(punctuation)
digs = list(digits)

dictionary.append(punc)
dictionary.append(digs)
print(len(dictionary))