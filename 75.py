from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    import collections

    counter = collections.Counter(nums)
    start = 0
    for i in range(counter[0]):
        nums[start] = 0
        start += 1
    for j in range(counter[1]):
        nums[start] = 1
        start += 1
    for k in range(counter[2]):
        nums[start] = 2
        start += 1