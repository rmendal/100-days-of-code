"""Calculate the dictionary word that would have the most value in Scrabble (https://en.wikipedia.org/wiki/Scrabble).
Follow the methods. First write a function to read in dictionary.txt (DICTIONARY constant) and return a list of words.
Second write a function that receives a word and calculates its value. Use the scores stored in LETTER_SCORES.
With these two pieces in place, write a third function that takes a list of words and returns the word with the highest
value. Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""
import re
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f: # open the file, read it, assign it to content
        content = f.read()

    """  list comporehension for words in content. If I return just this it would format like 
    '\n', 'U', 'N', 'E', 'X', 'E', 'C', 'R', 'A', 'T', 'E', 'D', '\n' also remove 2 hyphens in the list
    """
    content = [words.strip('-') for words in content]

    """ put the contents of content into an empty string. This will output all words with line breaks after each but
    still not in a python list.
    """
    content = ''.join(content)

    """ using regular expression library and the findall method looks for all words in the string and puts them in a 
    list which is exactly what we want here
    """
    words_list = re.findall(r'\w+', content)

    return words_list # returns the list


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    word = word.upper() # makes the word all upper case
    word = list(word) # breaks the word into a list so each char can be compared
    word_score = 0 # var for total score

    for k, v in LETTER_SCORES.items(): # for loop for each key and corresponding value in the dict
        for chars in word: # to iterate over each character in the given word
            if chars in k: # if the chars in word are in the dict keys
                word_score += v # add the corresponding dict value to word_score

    return word_score # return the final word_score


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    words = [x.upper() for x in list(words)]  # converts the tuple to a list and performs upper on it
    max_score = 0
    word_iter = 0
    best_word = ''

    while word_iter < len(words):
        word_score = 0
        word = words.pop()  # removes the last item in the list and assigns it to word as a string
        for k, v in LETTER_SCORES.items():  # for loop for each key and corresponding value in the dict
            for chars in word:  # to iterate over each character in the given word
                if chars in k:  # if the chars in word are in the dict keys
                    word_score += v  # add the corresponding dict value to word_score
                    if word_score > max_score: # this if holds onto the best word and score
                        max_score = word_score
                        best_word = word
        word_iter += 1
    return best_word.lower()  # returns the highest scoring word in lower case to appease the tests xP


test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
print(max_word_value(test_words))

#TESTS
"""
#from wordvalue import load_words, calc_word_value, max_word_value

words = load_words()


def test_load_words():    
    assert len(words) == 235886
    assert words[0] == 'A'
    assert words[-1] == 'Zyzzogeton'
    assert ' ' not in ''.join(words)


def test_calc_word_value():
    assert calc_word_value('bob') == 7
    assert calc_word_value('JuliaN') == 13
    assert calc_word_value('PyBites') == 14
    assert calc_word_value('benzalphenylhydrazone') == 56


def test_max_word_value():
    test_words = ('bob', 'julian', 'pybites', 'quit', 'barbeque')
    assert max_word_value(test_words) == 'barbeque'
    assert max_word_value(words[20000:21000]) == 'benzalphenylhydrazone'

"""