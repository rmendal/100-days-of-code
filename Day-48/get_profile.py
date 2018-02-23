'''
Write a function called get_profile that can only allows 2 keyword arguments: name and profession which default to
julian and programmer respectively.

The function does nothing fancy, just return a str: name is a profession.

The point is to limit the interface of this function and you'll see Python makes it very easy ... have fun!
'''
import pytest

# the star in the args section FORCES both kwargs to be mandatory. So if you pass one kwarg it will fail.
def get_profile(*, name='julian', profession='programmer'):

    return name +  ' is a '  + profession

print(get_profile())