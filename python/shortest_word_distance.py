from typing import List


def shortest_word_distance(wordsDict: List[str], word1: str, word2: str):
    '''
    Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
    return the shortest distance between these two words in the list
    >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    3
    >>> shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
    1
    >>> shortest_word_distance(["a", "a", "b", "b"], "a", "b")
    1
    '''
    idx1 = -1
    idx2 = -1
    shortest_distance = len(wordsDict)
    for idx, word in enumerate(wordsDict):
        if word == word1:
            idx1 = idx
        if word == word2:
            idx2 = idx
        if idx1 >= 0 and idx2 >= 0:
            if abs(idx1 - idx2) < shortest_distance:
                shortest_distance = abs(idx1 - idx2)
    print(shortest_distance)
