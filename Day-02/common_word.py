"""Write a function that returns the most common (non stop) word in Harry Potter.
Make sure you strip out non-alphanumeric characters and your function should return a tuple of
(most_common_word, frequency). Both text and stopwords are provided in the template. There are actually
two right answers, check the tests ... Have fun!"""

import os
import urllib.request
import re
from collections import Counter

# data provided
stopwords_file = os.path.join('/home/rob/git/100-days-of-code/Day-02/tmp', 'stopwords')
harry_text = os.path.join('/home/rob/git/100-days-of-code/Day-02/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)

def get_harry_most_common_word():
    """open the files, clean the potter text and put it in a string.
    iterate over both files and find the most used word as well as total it's occurance"""

    #harry_file = open(harry_text).read()
    stop_file = [words.splitlines() for words in open(stopwords_file).read().split(" ")]
    harry_read = [words.strip('\'.?\",;:-!') and words.replace('\n', ' ') for words in open(harry_text).read().lower()]
    harry_cleaned = ''.join(harry_read)

#    for words in stop_file:
#        if words in harry_read:
#            harry_read.remove()
#            print(harry_read)
    print(harry_cleaned)


    #print(stop_file)
    #print(harry_read)


get_harry_most_common_word()
