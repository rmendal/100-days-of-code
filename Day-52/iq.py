'''
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out which one of the given characters differs from the others. He
observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among
non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details

SOLUTION
import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def get_index_different_char(chars):
    matches, no_matches = [], []
    for i, char in enumerate(chars):
        if str(char).lower() in alphanumeric_chars:
            matches.append(i)
        else:
            no_matches.append(i)
    return matches[0] if len(matches) == 1 else no_matches[0]

'''

import string

alnum = list(string.ascii_letters + string.digits) #<- correct
chars = list(string.punctuation + string.whitespace) #<- Unnecessary / Only used alphnumeric

lis = ['a', 'b', 'c', '^', 'd']



print([x for x in lis.index(alnum)]) #<- Incorrect


for i, j in enumerate(lis): #<- correct
    alist = [] #correct
    clist = [] #correct
    for a, c in zip(alnum, chars): #<- incorrect due to only needing one list alnum
        if j in a: #<- should be if lis in alnum:
            alist.append(j) #<- append(i), the index number
            if len(alist) > 1: #<- incorrect
                break #<- incorrect
        else:
            print(i) #<- incorrect, should be clist.append(i)
            break #<- incorrect
        if j in c: #<- incorrect
            clist.append(j) #<- incorrect
            if len(clist) > 1: #<- incorrect
                break #<- incorrect
        else: #<- incorrect
            print(i) #<- incorrect
            break #<- incorrect

    #return alist[0] is len(alist) == 1 else clist[0]


