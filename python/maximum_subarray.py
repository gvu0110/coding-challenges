from typing import List
from decimal import Decimal


def maximum_subarray_dynamic_programming(nums: List[int]) -> int:
    '''
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.
    >>> print(maximum_subarray_dynamic_programming([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    6
    >>> print(maximum_subarray_dynamic_programming([1]))
    1
    >>> print(maximum_subarray_dynamic_programming([5, 4, -1, 7, 8]))
    23
    '''
    # Initialize our variables using the first element
    current_sum = nums[0]
    max_sum = nums[0]

    # Start with the 2nd element since we already used the first one
    for num in nums[1:]:
        # If current_sum is negative, throw it away. Otherwise, keep adding to it
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def maximum_subarray_divide_and_conquer(nums: List[int]) -> int:
    '''
    >>> print(maximum_subarray_divide_and_conquer([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    6
    >>> print(maximum_subarray_divide_and_conquer([1]))
    1
    >>> print(maximum_subarray_divide_and_conquer([5, 4, -1, 7, 8]))
    23
    '''
    left, right = 0, len(nums) - 1
    return find_max_sum_subarray(nums, left, right)


def find_max_sum_subarray(nums: List[int], left: int, right: int) -> int:
    if left > right:
        return Decimal('-Infinity')

    middle = (left + right) // 2

    # Iterate from the middle to the left
    current_sum = 0
    max_sum_left = 0
    for i in range(middle - 1, left - 1, -1):
        current_sum += nums[i]
        max_sum_left = max(max_sum_left, current_sum)

    # Reset current sum and iterate from the middle to the right
    current_sum = 0
    max_sum_right = 0
    for i in range(middle + 1, right + 1):
        current_sum += nums[i]
        max_sum_right = max(max_sum_right, current_sum)

    # The max_sum uses the middle element and the best possible sum from each half
    max_sum_combined = max_sum_left + nums[middle] + max_sum_right

    return max(max_sum_combined, max(find_max_sum_subarray(nums, left, middle - 1), find_max_sum_subarray(nums, middle + 1, right)))
