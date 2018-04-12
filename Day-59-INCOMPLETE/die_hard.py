'''
Given a listing of files of our community branch determine who PR'd (= submitted pull request) the most
(excluding PyBites) and what challenge is the most popular (PR'd) as per snapshot of today (8th of Dec 2017).

See preparation done in the code template below. Replace pass with your code to make the test pass. Good luck and have
fun!
'''

"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

# prep

tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files():
    """return a generator of dir names reading in `tempfile`

       `tempfile` has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(tempfile) as f:
        lines = f.readlines() # readlines puts each line from the file into it's own index in a list


    true_lines = [i.strip('\n') for i in lines if 'True' in i] # strip the newline char and filter for True


    print(true_lines)

    #print(true_lines)

def diehard_pybites():
    """return a Stats namedtuple (defined above) that has the user that
       most PR'd and a tuple of most popular challenge = (challenge, num_prs)
       see the test for the exected values"""
    #users, popular_challenges = Counter(), Counter()