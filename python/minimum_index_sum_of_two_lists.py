from typing import List, Dict


def minimum_index_sum_of_two_lists(list1: List[str], list2: List[str]):
    '''
    Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
    You need to help them find out their common interest with the least list index sum.
    If there is a choice tie between answers, output all of them with no order requirement.
    You could assume there always exists an answer.
    >>> list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    >>> list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    >>> minimum_index_sum_of_two_lists(list1, list2)
    ['Shogun']
    >>> list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    >>> list2 = ["KFC", "Shogun", "Burger King"]
    >>> minimum_index_sum_of_two_lists(list1, list2)
    ['Shogun']
    >>> list1 = ["a", "b", "c", "d"]
    >>> list2 = ["c", "b", "a"]
    >>> minimum_index_sum_of_two_lists(list1, list2)
    ['c', 'b', 'a']
    '''
    result = []
    min_index_sum = len(list1) + len(list2)
    interest_to_index: Dict[str, int] = {}
    for idx, interest in enumerate(list1):
        interest_to_index[interest] = idx

    for idx, interest in enumerate(list2):
        if interest in interest_to_index:
            index_sum = idx + interest_to_index[interest]
            if min_index_sum > index_sum:
                min_index_sum = index_sum
                result.clear()

            if min_index_sum == index_sum:
                result.append(interest)
    print(result)
