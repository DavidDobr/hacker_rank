import string

def constructable(s, chars, with_replacement = True):
    """
    Find out whether string s can be constructed using characters form chars
    @param s: the string to be checked for constructubility
    @param chars: characters to be used as building blocks of construction
    @param with_replacement: determines whether construction uses replacement \
for constructing s out of chars

    @returns: bool (True/False)
    """
    s = str(s)
    chars = str(chars)
    # create a list asserting whether each character of s is in chars
    b = [c in chars for c in s]
    # return True if all characters are in chars; o/w return False
    return all(b)

def fun(s):
    """ Validate whether a string is a valid email

    Valid email addresses must follow these rules:
    - It must have the username@websitename.extension format type.
    - The username can only contain letters, digits, dashes and underscores.
    - The website name can only have letters and digits.
    - The maximum length of the extension is 3.
    """
    s = s.split('@')
    if len(s) != 2:
        # check that s contains exactly one @
        return False

    username = s[0] # because s was split by @

    if s[1].count('.') != 1:
        # check that there's exactly one dot after @
        return False
    else:
        websitename, extension = s[1].split('.')

    # now check whether username, websitename, extension have correct format




    return s

print(fun('@icloud.com'))
print(fun('john@icloud.com'))
