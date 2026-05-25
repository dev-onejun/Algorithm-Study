"""
" https://leetcode.com/problems/contains-duplicate/
"
" Return True iff any value in `nums` appears at least twice.
"
" Constraints:
"   1 <= len(nums) <= 10^5
"   -10^9 <= nums[i] <= 10^9
"""

from typing import List


# ----- Stage 1: brute force -- O(n^2) time, O(1) space ---------------------
def contains_duplicate_bruteforce(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ----- Stage 2: sort + adjacent scan -- O(n log n) time, O(1) extra --------
def contains_duplicate_sort(nums: List[int]) -> bool:
    s = sorted(nums)  # use .sort() on a copy if you must keep input intact
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False


# ----- Stage 3: hash set with early exit -- O(n) time, O(n) space (optimum)
def contains_duplicate_set(nums: List[int]) -> bool:
    seen = set()
    for v in nums:
        if v in seen:
            return True
        seen.add(v)
    return False


# ----- User submission #1: counter dict ------------------------------------
def contains_duplicate_user_counter(nums: List[int]) -> bool:
    dict_table = {num: 0 for num in nums}
    for num in nums:
        dict_table[num] += 1
        if dict_table[num] > 1:
            return True
    return False


# ----- User submission #2: len(set) vs len(list) ---------------------------
def contains_duplicate_user_setlen(nums: List[int]) -> bool:
    num_set = len(set(nums))
    num_list = len(nums)
    if num_set != num_list:
        return True
    else:
        return False
