#!/usr/bin/env python3

from string import punctuation, digits
from random import choices, choice
import argparse

#parser = argparse.ArgumentParser(description='Generate secure passwords.')


chars = punctuation #pulls characters from string lib
nums = digits #pulls numbers from string library

with open('dictionary.txt') as f:
    dictionary = f.read().split()

def pwd_gen():

    for i in range(5): #Makes 5 passwords
        pwd = (choices(dictionary, k=2)) #Pulls 2 random words form the dictionary. k can be changed depending on security need
        pwd = [''.join(choices(nums)) + s + ''.join(choices(chars)) for s in pwd] #Add random char and num to beginning/end of each word
        pwd = [''.join(choices(chars)) + m + ''.join(choices(nums)) for m in pwd] #Add random char and num to beginning/end of each word
        pwd = ''.join(pwd) #Gets the pwd out of the list and into a string
        pwd = ''.join(choice([k.upper(), k]) for k in pwd)  # Capitalize random letters in each dict word

        print(pwd, '\r')

    return '' # return empty string because I don't want to see 'None' on the return

print(pwd_gen())
