from typing import List, Generator
import re


class StringIterator(object):
    def __init__(self, compressedString: str):
        def get_string_generator(compressed_string: str) -> Generator:
            for string in re.findall(r'\D\d+', compressed_string):
                letter = string[0]
                amount = int(string[1:])

                for _ in range(amount):
                    yield letter

        self.string_generator: Generator = get_string_generator(compressedString)
        self._exhausted = False
        self._cache_next_item()

    def _cache_next_item(self):
        try:
            self.next_item = next(self.string_generator)
        except StopIteration:
            self.next_item = ' '
            self._exhausted = True

    def next(self) -> str:
        next_item = self.next_item
        self._cache_next_item()
        return next_item

    def hasNext(self) -> bool:
        return not self._exhausted


def design_compressed_string_iterator(compressedString: str, methods: List[str]):
    """
    Design and implement a data structure for a compressed string iterator.
    The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.
    Implement the StringIterator class:
    - next(): returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
    - hasNext(): returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.
    >>> compressedString = "L1e2t1C1o1d1e1"
    >>> methods = ["next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next"]
    >>> design_compressed_string_iterator(compressedString, methods)
    L
    e
    e
    t
    C
    o
    True
    d
    True
    e
    False
    <BLANKLINE>
    >>> compressedString = "x6"
    >>> methods = ["next", "next", "next", "hasNext", "next", "next", "next", "next", "next", "next", "next", "hasNext", "next"]
    >>> design_compressed_string_iterator(compressedString, methods)
    x
    x
    x
    True
    x
    x
    x
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    False
    <BLANKLINE>
    """
    string_iterator = StringIterator(compressedString)
    for method in methods:
        print(getattr(string_iterator, method)())
