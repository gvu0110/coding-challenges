from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    '''
    Given an array of integers nums and an integer target, return indexes of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    >>> nums = [2, 7, 11, 15]
    >>> target = 9
    >>> print(two_sum(nums, target))
    [0, 1]
    >>> nums = [3, 2, 4]
    >>> target = 6
    >>> print(two_sum(nums, target))
    [1, 2]
    >>> nums = [3, 3]
    >>> target = 6
    >>> print(two_sum(nums, target))
    [0, 1]
    '''
    remainder_to_index = {}
    for i, num in enumerate(nums):
        if num not in remainder_to_index:
            remainder = target - num
            remainder_to_index[remainder] = i
        else:
            return [remainder_to_index[num], i]
