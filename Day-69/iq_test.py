'''The most frequent task in this test is to find out which one of the given characters differs from the others. He
observed that one char usually differs from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs a program to find the different one (the alphanumeric among
non-alphanumerics or vice versa) among the given characters.

Complete get_index_different_char to meet this goal. It receives a chars list and returns an int index (zero-based).

Just to be clear, alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)'''

from string import ascii_letters, digits

alnum = list(ascii_letters + digits)

def get_index_different_char(chars):
    chars = list(chars)
    al, ch = [],[]
    for pos, item in enumerate(chars):
        if item in alnum:
            al.append(pos)
        else:
            ch.append(pos)
    if len(ch) == 1:
        print(ch[0])
    else:
        print(al[0])


if __name__ == '__main__':
    get_index_different_char('abc.g')
