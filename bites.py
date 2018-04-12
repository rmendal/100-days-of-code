"""Complete the validate_password function below. It takes a password str and validates that it:

is between 6 and 12 chars long (both inclusive)
has at least 1 digit [0-9]
has at least two lowercase chars [a-z]
has at least one uppercase char [A-Z]
has at least one punctuation char (use: PUNCTUATION_CHARS)
Has not been used before (use: used_passwords)
If the password matches all criteria the function should store the password in used_passwords and return True."""


from string import punctuation, digits, ascii_lowercase, ascii_uppercase

digis = list(str(digits))
lower = list(ascii_lowercase)
upper = list(ascii_uppercase)
PUNCTUATION_CHARS = list(punctuation)
used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if password in used_passwords:
        return 'Password already in list'
    else:
        password = list(password)

        #TODO: First ensure proper length between 6 & 12
        if len(password) < 6 or len(password) > 12:
            return 'Password is incorrect length'
        #TODO: Begin ensuring password meets criteria
        else:
            for x in password:
                #TODO: Ensure password contains AT LEAST 2 digits
                if x in digis:
                    i++



#validate_password('acDE*22&')
print(used_passwords)