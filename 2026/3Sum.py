"""
" https://leetcode.com/problems/3sum/
"
" Return all unique triplets [a, b, c] from `nums` with a + b + c == 0.
" The solution set must not contain duplicate triplets (order irrelevant).
"
" Constraints:
"   3 <= len(nums) <= 3000
"   -10^5 <= nums[i] <= 10^5
"
" This is the 3-element generalization of Two Sum II: sort the array, fix the
" smallest element, then solve a sorted two-sum for the other two. The new
" wrinkle is de-duplication — skipping repeated values so the same triplet
" isn't emitted twice.
"""

from typing import List


# ----- Stage 1: brute force, dedup via a set -- O(n^3) time ----------------
def three_sum_brute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(t) for t in res]


# ----- Stage 2: sort + hash set for the inner two-sum -- O(n^2) time, O(n) -
# Insight: fix anchor i, then it's Two Sum (hash-set form) over the suffix for
# the value -arr[i]. Sorting first makes each found triplet already ordered,
# so a result set dedups cleanly.
def three_sum_hashset(nums: List[int]) -> List[List[int]]:
    arr = sorted(nums)
    n = len(arr)
    res = set()
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        seen = set()
        for j in range(i + 1, n):
            comp = -arr[i] - arr[j]
            if comp in seen:
                res.add((arr[i], comp, arr[j]))  # ordered by construction
            seen.add(arr[j])
    return [list(t) for t in res]


# ----- Stage 3: sort + two pointers -- O(n^2) time, O(1) extra (optimum) ---
# Insight: same as Two Sum II for the inner pair, no hash set needed. Dedup by
# skipping equal anchors, and equal lo/hi values after each hit. Break early
# once arr[i] > 0 (no way three sorted values >= a positive sum to zero).
def three_sum_twoptr(nums: List[int]) -> List[List[int]]:
    arr = sorted(nums)
    n = len(arr)
    res = []
    for i in range(n - 2):
        if arr[i] > 0:
            break
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = arr[i] + arr[lo] + arr[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([arr[i], arr[lo], arr[hi]])
                lo += 1
                hi -= 1
                while lo < hi and arr[lo] == arr[lo - 1]:
                    lo += 1
                while lo < hi and arr[hi] == arr[hi + 1]:
                    hi -= 1
    return res
