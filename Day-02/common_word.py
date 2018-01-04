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

    #Create single list of words from the stop words file
    stop_file = [words for words in open(stopwords_file).read()]
    stop_file = ''.join(stop_file)
    stop_list = re.findall(r'\w+', stop_file)

    #Create single list of words in Harry Potter text and clean it from non-alnum chars
    words = [words.strip('\'.?\",;:-!') and words.replace('\n', ' ') for words in open(harry_text).read().lower()]
    words = ''.join(words)
    words_list = re.findall(r'\w+', words)

    #Create final single list for potter words not in stop words
    last_list = [x for x in words_list if x not in stop_list]

    #Finds the final word and counts it's occurance
    top_word = Counter(last_list).most_common(1).pop()
    return (top_word)

print(get_harry_most_common_word())
