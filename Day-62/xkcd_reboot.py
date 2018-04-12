#!/usr/bin/env python3

'''
You could encrypt all the passwords in the text file and add the hash of generated passwords to the file as they
are being created.

Every time a new password is created ensure that it's hash doesn't exist in the file. This way every password is unique
'''

from string import punctuation, digits
from random import choices, choice
from hashlib import sha3_512

sha = sha3_512 #pulls SHA3 512 from hashlib
nums, chars = digits, punctuation #pulls digits and characters from string lib

def pwd_gen(pwd_num, *args):
    '''Generates passwords based on the rules below. Then passes the list to the hash check func. It then receives the
    list back which will either be the same or shorter if the hash was found in the hash file.

    If the list comes back less than the original length new passwords need to be generated/checked to meet the list
    requirement. Repeat this process until the list is the requested length and meets the hash check requirements.'''
    if len(args) > 0:
        pass
    else:
        pwd_list = [] # Empty list to append the passwords to.

    with open('dictionary.txt') as f: #Open the dict file and add the words to a list
        dictionary = f.read().split()

    for i in range(pwd_num): #For loop for the range of passwords needed.
        pwd = (choices(dictionary, k=2)) #Pulls 2 random words from the dictionary. k can be changed depending on security need
        pwd = [''.join(choices(nums)) + s + ''.join(choices(chars)) for s in pwd] #Add random char and num to beginning/end of each word
        pwd = [''.join(choices(chars)) + m + ''.join(choices(nums)) for m in pwd] #Add random char and num to beginning/end of each word
        pwd = ''.join(pwd) #Gets the pwd out of the list and into a string
        pwd = ''.join(choice([k.upper(), k]) for k in pwd)  # Capitalize random letters in each dict word
        pwd_list.append(pwd) #Append each password created to the list.

    hash_check(pwd_list, len(pwd_list))

    return None # Return the passwords once all is said and done. Right now, none.



def hash_check(pwd_list, pwd_list_len):
    '''Encrypt the passwords here and check them against the hash file. If they are not in the hash file, add the
    hash(es) to the file and close it, then send the passwords back up to the pwd_gen func to print them out.

    If the hash IS found in the hash file remove it from the pwd list and send back the final list.'''

    hash_list = [] #Empty list to hold hashes.

    #Open the file and put the existing hashes into a list
    with open('hash.txt') as h: #Open the hash file and add it's contents to a list.
        hash_file = h.read().split()

    #Create the hash_list from the password list
    for x in pwd_list:
        hash_list.append(sha(x.encode('utf-8')).hexdigest())

    #Iterate over the hash list and hash file list. If/Else to remove any dupes from the pwd list and write unique
    #hashes to has file.
    hash_dict = dict(zip(hash_list, pwd_list))

    for k, v in hash_dict.items():
        if k in hash_file:
            pwd_list.remove(v)
        else:
            with open('hash.txt', 'a') as h:
                h.write(k + '\r')

    #TODO: Return the pwd list, in whole or in part to the pwd_gen func
    if pwd_list_len < len(pwd_list):
        pwd_gen(len(pwd_list), pwd_list)
    else:
        pwd_list = ''.join(pwd_list)
        return print(pwd_list, '\r')

if __name__=="__main__":
    pwds = int(input('How many passwords would you like to generate? '))
    pwd_gen(pwds)
