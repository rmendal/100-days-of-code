'''
Write a function called get_profile that takes:
- a required name,
- a required age,
- one or more optional sports (args),
- one or more optional awards (keyword args).

Do the following validations:
- if age is not an int raise a ValueError,
- if more than 5 sports are provided raise a ValueError.

Some examples how your function can be called (see also the tests):

get_profile('tim', 36)
get_profile('tim', 36, 'tennis', 'basketball')
get_profile('tim', 36, 'tennis', 'basketball', champ='helped out team in crisis')

'''

def get_profile(name, age, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError
    if len(args) > 5:
        raise ValueError
    sports = list(args)
    output = {'name':name, 'age':age}
    if args:
        output.update({'sports':sorted(sports)})
    if kwargs:
        output.update({'awards':kwargs})
    return output
