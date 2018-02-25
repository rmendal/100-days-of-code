'''
Iterate over the given names and countries lists. In each loop print the value of each and also the counter of the loop
(starting at 1).

Here is the output you need to deliver. Ideally you use only one for loop.

The 2nd column should be exactly 10 chars wide aligning to the left (format magic):

       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico

https://docs.python.org/3.4/library/string.html#format-examples
Need to use enumerate but haven't a clue how to work it in. It produces a tuple which isn't ideal for printing. Am I to
break it out of the tuple before printing? That feels overly complicated considering the task but maybe it's right? Ex-
plore that option before getting too frustrated, despite it seeming convoluted.
'''

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

def enumerate_names_countries():
    #for i, (a, b) in enumerate(zip(alist, blist)):
    for index, (n, c) in enumerate(zip(names, countries), start=1): # zip allows iterating over 2 lists simultaneously
        print(str(index) + '.', '{:<10}'.format(n), c)

print(enumerate_names_countries())
