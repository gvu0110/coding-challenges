import string


def keypad_string(keys):
    '''
    Given a string consisting of 0-9, find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("2212")
    'ba'
    >>> keypad_string("2122222")
    'acb'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    keypad = key_pad_to_letter()
    s = ''
    result = ''
    for letter in keys:
        if len(s) > 0 and (s[-1] != letter or (s + letter) not in keypad):
            result += keypad[s]
            s = ''

        s += letter

    result += keypad[s]
    return result


def key_pad_to_letter():
    result = {
        '': '',
        '0': ' ',
        '1': '',
    }
    key = 2
    repeat = 1
    for letter in string.ascii_lowercase:
        if letter in {'r', 'y'}:
            max_repeat = 4
        else:
            max_repeat = 3

        result[str(key) * repeat] = letter
        repeat += 1
        if repeat > max_repeat:
            repeat = 1
            key += 1

    return result
