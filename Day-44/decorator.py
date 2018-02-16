'''Write a decorator called make_html that wraps text inside one or more html tags.
As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'): ...

- returns: <p><strong>I code with PyBites</strong></p>'''

from functools import wraps


def make_html(element):
    '''adding *args and **kwargs as arguments to the wrapped function and passing them on to the func call inside of the
    decorator. This makes it so you can decorate a function that accepts any number of positional or named arguments
    and it will still work correctly.
    '''
    def outer(x):
        @wraps(x)
        def wrapper(*args, **kwargs):
            return '<%s>%s</%s>' % (element, x(*args, **kwargs), element)
        return wrapper
    return outer

## TESTS ##
def test_make_html():
    @make_html('p')
    @make_html('strong')
    def get_text(text='I code with PyBites'):
        return text

    assert get_text() == '<p><strong>I code with PyBites</strong></p>'