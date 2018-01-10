"""Get the top 10 tags of PyBites. Our tests suppose you will use a collections.Counter - best practice and less code.
What are the PyBites guys most passionate about? See tests and you'll know the answer, then code your solution to make
them pass :)
"""
import os
import re
from collections import Counter
import urllib.request

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()

# start coding
def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable
       """
    '''TAG_HTML above sets up what to search for and content is the file to search then I set tags_list 
    to findall using TAG_HTML as the string to search and content as what to search through and finally call Counter
    against tags_list coupled with most_common(n) with n being defaulted to 10 per the function.
    '''
    tags_list = re.findall(TAG_HTML, content)
    return Counter(tags_list).most_common(n)



print(get_pybites_top_tags(10))

'''from tags import get_pybites_top_tags

def test_get_pybites_top_tags():
    expected = [('python', 79),
                ('learning', 79),
                ('codechallenges', 72),
                ('twitter', 62),
                ('tips', 61),
                ('flask', 52),
                ('news', 49),
                ('django', 37),
                ('code', 25),
                ('github', 24)]
    assert get_pybites_top_tags() == expected'''