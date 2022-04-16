from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    '''
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same.
    You must have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
    It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    >>> print(remove_duplicates_from_sorted_array([1, 1, 2]))
    2
    >>> print(remove_duplicates_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    5
    >>> print(remove_duplicates_from_sorted_array([0, 0, 2, 2, 3]))
    3
    '''
    # Declare an index pointer to mark the position for unique element
    index = 0
    for i in range(len(nums)):
        if nums[i] != nums[index]:
            # Move index pointer to the next position
            index += 1

            # Replace the index position with the current value
            nums[index] = nums[i]

    return index + 1
