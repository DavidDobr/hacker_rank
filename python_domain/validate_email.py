
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
