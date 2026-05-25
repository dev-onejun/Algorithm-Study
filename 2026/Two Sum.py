"""
" https://leetcode.com/problems/two-sum/
"
" Given an array `nums` and `target`, return indices of the two numbers
" that add up to `target`. Exactly one solution exists; no element reused.
"
" Constraints:
"   2 <= len(nums) <= 10^4
"   -10^9 <= nums[i], target <= 10^9
"""

from typing import List


# ----- Stage 1: brute force -- O(n^2) time, O(1) extra space ---------------
def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ----- Stage 2: two-pass hash map -- O(n) time, O(n) space -----------------
def two_sum_twopass(nums: List[int], target: int) -> List[int]:
    index_of = {}
    for i, v in enumerate(nums):
        index_of[v] = i  # later duplicates overwrite — fine, we just need any valid pair

    for i, v in enumerate(nums):
        j = index_of.get(target - v)
        if j is not None and j != i:
            return [i, j]
    return []


# ----- User's submission ---------------------------------------------------
def two_sum_user(nums: List[int], target: int) -> List[int]:
    dict_table = {i: target - nums[i] for i in range(len(nums))}
    dict_table2 = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        try:
            j = dict_table2[dict_table[i]]
            if i == j:
                continue
            break
        except KeyError:
            continue
    return [i, j]


# ----- Stage 3: one-pass hash map -- O(n) time, O(n) space (optimum) -------
def two_sum_onepass(nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index seen so far
    for i, v in enumerate(nums):
        complement = target - v
        if complement in seen:
            return [seen[complement], i]
        seen[v] = i
    return []
