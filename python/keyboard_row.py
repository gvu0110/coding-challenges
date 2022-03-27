from typing import List, Set


def keyboard_row(words: List[str]):
    '''
    Given an array of strings words, return words that can be typed using letters of the alphabet on only one row of American keyboard
    In the American keyboard:
    - The first row consists of the characters "qwertyuiop"
    - The second row consists of the characters "asdfghjkl"
    - The third row consists of the characters "zxcvbnm"
    >>> keyboard_row(["Hello", "Alaska", "Dad", "Peace"])
    ['Alaska', 'Dad']
    >>> keyboard_row(["omk"])
    []
    >>> keyboard_row(["adsdf", "sfd"])
    ['adsdf', 'sfd']
    '''
    keyboard_rows: List[Set[str]] = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
    result: List[str] = []
    for word in words:
        letters: Set[str] = set(word.lower())
        for row in keyboard_rows:
            if not letters - row:
                result.append(word)
    print(result)
