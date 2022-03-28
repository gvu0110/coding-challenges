from collections import defaultdict, Counter
from typing import List, Set, Dict
import string


def shortest_completing_word(licensePlate: str, words: List[str]):
    '''
    Given a string licensePlate and an array of strings words (1 <= words[i].length <= 15), find the shortest completing word in words.
    A completing word is a word that:
    - Contains all the letters in licensePlate
    - Ignores numbers and spaces in licensePlate
    - Treats letters as case insensitive.
    - If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
    Return the shortest completing word in words. It is guaranteed an answer exists.
    If there are multiple shortest completing words, return the first one that occurs in words.
    >>> licensePlate = "1s3 PSt"
    >>> words = ["step", "steps", "stripe", "stepple"]
    >>> print(shortest_completing_word(licensePlate, words))
    steps
    >>> licensePlate = "1s3 456"
    >>> words = ["looks", "pest", "stew", "show"]
    >>> print(shortest_completing_word(licensePlate, words))
    pest
    '''
    alphabet_letters: Set[str] = set(string.ascii_lowercase)
    letter_to_amount: Dict[str, int] = defaultdict(int)
    for c in licensePlate:
        if c.lower() in alphabet_letters:
            letter_to_amount[c.lower()] += 1

    min_word_length = 15
    for word in words:
        letter_counter = Counter(word)
        for letter, amount in letter_to_amount.items():
            if letter not in letter_counter or letter_counter[letter] < amount:
                found_word = False
                break
            found_word = True

        if found_word and min_word_length > len(word):
            min_word_length = len(word)
            result = word
    return result
