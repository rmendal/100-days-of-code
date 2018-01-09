"""In this bite you learn to catch/raise exceptions. Write a simple division function meeting the following requirements:

1. when denominator is 0 catch the corresponding exception and return 0.
2. when numerator or denominator are not of the right type reraise the corresponding exception.
3. if the result of the division (after surviving the exceptions) is negative, raise a ValueError

As always see the pytests to see how your code will be tested. Have fun!"""

import pytest
from math import isnan

def positive_divide(numerator, denominator):
    try:
        if denominator == 0: # Returns 0 if the denominator is 0 instead of throwing the divide by zero exception
            return 0
        elif (numerator / denominator) < 0:
            raise ValueError('Negative number!') # Raise a ValueError if the result is negative.
        elif isnan(numerator) == True or \
                isnan(denominator) == True: #If numerator or denominator are Not A Number (NaN) raise type error
            raise TypeError
        else:
            return (numerator / denominator) # If the division doesn't trigger an error return the result
    finally:
        pass

#####TESTS#####

def test_positive_divide_good_values():
    assert positive_divide(1, 2) == 0.5
    assert positive_divide(1, 0) == 0
    assert positive_divide(-1, -2) == 0.5
    assert positive_divide(1.5, 2) == 0.75


def test_positive_divide_exceptions():
    try:
        positive_divide(2, 0)
    except ZeroDivisionError:
        pytest.fail("Unexpected ZeroDivisionError!")
    with pytest.raises(TypeError):
        positive_divide(1, 's')
        positive_divide([], 2)
    with pytest.raises(ValueError):
        positive_divide(1, -2)
        positive_divide(-1, 2)

print(test_positive_divide_exceptions())