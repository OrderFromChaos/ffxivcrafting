def validate_input(prompt, validf, message=''):
    # prompt: how to ask for the the input
    # validf may either be an iterable or function
    # message: what to return if validation fails. if empty and list, return valid string list.
    if callable(validf):
        validtype = 1
    elif hasattr(validf, '__iter__'):
        validtype = 0
    else:
        raise Exception(('Unrecognized object to validate with:', validf))
    
    currinput = input(prompt + ' ')
    if validtype == 0:
        while currinput not in validf:
            if message:
                print(message)
            else:
                print('    Invalid input. String must be a member of:', validf)
            currinput = input(prompt + ' ')
    if validtype == 1:
        while not validf(currinput):
            if message:
                print(message)
            else:
                print('    Invalid input.')
            currinput = input(prompt + ' ')
    return currinput

def int_validator(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def coord_validator(string):
    import re
    
    findnums= re.compile(r'(\d+(\.\d)?\s*,\s*\d+(\.\d)?)')
    matches = re.findall(findnums, string)
    if matches:
        return True
    else:
        return False