from typing import List


def sentence_similarity(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    '''
    Given two sentences sentence1 and sentence2 each represented as a string array.
    Given an array of string pairs similarPairs where similarPairs[j] = [xi, yi] indicates that the two words xi and yi are similar.
    Return true if sentence1 and sentence2 are similar, or false if they are not similar.
    Two sentences are similar if:
    - They have the same length (i.e., the same number of words)
    - sentence1[i] and sentence2[i] are similar.
    Notice that a word is always similar to itself, also notice that the similarity relation is not transitive.
    For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
    >>> sentence1 = ["great", "acting", "skills"]
    >>> sentence2 = ["fine", "drama", "talent"]
    >>> similarPairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    >>> print(sentence_similarity(sentence1, sentence2, similarPairs))
    True
    >>> sentence1 = ["great"]
    >>> sentence2 = ["great"]
    >>> similarPairs = []
    >>> print(sentence_similarity(sentence1, sentence2, similarPairs))
    True
    >>> sentence1 = ["great"]
    >>> sentence2 = ["doubleplus", "good"]
    >>> similarPairs = [["great", "doubleplus"]]
    >>> print(sentence_similarity(sentence1, sentence2, similarPairs))
    False
    '''
    if sentence1 == sentence2:
        return True

    if len(sentence1) != len(sentence2):
        return False

    similar_pairs = [set(pair) for pair in similarPairs]
    for i in range(len(sentence1)):
        if sentence1[i] != sentence2[i]:
            pair = set([sentence1[i], sentence2[i]])
            if pair not in similar_pairs:
                return False

    return True
