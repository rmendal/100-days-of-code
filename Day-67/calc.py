'''
$ python calculator.py --add 1 2 3
6.0
$ python calculator.py --sub 10 6 2
2.0
$ python calculator.py --mul 3 3 3
27.0
$ python calculator.py --div 8 5 7
0.23

https://stackoverflow.com/questions/13840379/how-can-i-multiply-all-items-in-a-list-together-with-python
'''

import argparse
from functools import reduce


def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals
       check out the math library for easier versions of these"""
    numbers = list(numbers)
    if operation in ['-a', '--add']:
        return round(sum(numbers), 2)

    elif operation in ['-s', '--sub']:
        return round(reduce(lambda x, y: x - y, numbers), 2)

    elif operation in ['-m', '--mul']:
        return round(reduce(lambda x, y: x * y, numbers), 2)

    elif operation in ['-d', '--div']:
        return round(reduce(lambda x, y: x / y, numbers), 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object"""
    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument("-a", "--add", help="Sums numbers", type=int, nargs='+')
    parser.add_argument("-s", "--sub", help="Subtracts numbers", type=int, nargs='+')
    parser.add_argument("-m", "--mul", help="Multiplies numbers", type=int, nargs='+')
    parser.add_argument("-d", "--div", help="Divides numbers", type=int, nargs='+')
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)
