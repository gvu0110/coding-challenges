from typing import List


def remove_element(nums: List[int], val: int) -> int:
    '''
    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
    The relative order of the elements may be changed.
    You must instead have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    >>> nums = [3, 2, 2, 3]
    >>> val = 3
    >>> print(remove_element(nums, val))
    2
    >>> nums = [0, 1, 2, 2, 3, 0, 4, 2]
    >>> val = 2
    >>> print(remove_element(nums, val))
    5
    '''
    # Declare an index pointer to mark the position of val
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            # Swap the index value with the current value
            temp = nums[index]
            nums[index] = nums[i]
            nums[i] = temp

            # Move the index pointer to the next position
            index += 1

    return index
