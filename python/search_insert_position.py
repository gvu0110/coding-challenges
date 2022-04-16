from typing import List


def search_insert_position(nums: List[int], target: int) -> int:
    '''
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
    >>> nums = [1, 3, 5, 6]
    >>> target = 5
    >>> print(search_insert_position(nums, target))
    2
    >>> nums = [1, 3, 5, 6]
    >>> target = 2
    >>> print(search_insert_position(nums, target))
    1
    >>> nums = [1, 3, 5, 6]
    >>> target = 7
    >>> print(search_insert_position(nums, target))
    4
    '''
    left, right = 0, len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return left + 1 if nums[left] < target else left
