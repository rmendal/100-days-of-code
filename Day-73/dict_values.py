from itertools import permutations
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    draw_perms = _get_permutations_draw(draw)
    print(draw_perms)
    return print([i for i in draw_perms if i in dictionary])


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return [''.join(i) for i in list(permutations(draw.lower()))]


if __name__ == '__main__':
    print(get_possible_dict_words("TIIGTTL"))