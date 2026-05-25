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


"""
" ============================================================================
" Review of submitted solutions — 2026-05-25
" ============================================================================
"
" Two solutions submitted: a commented counter-dict version and an active
" `len(set) != len(list)` version.
"
" Stress at n=100_000 (ms):
"                          distinct   dup-at-end   dup-at-1
"   set (Stage 3 optimum)    11.04        11.31       0.36   ← short-circuits
"   user-counter             18.92        17.81       7.81
"   user-setlen               6.22         5.44       7.52   ← fastest on no-dup
"
" --- Solution #1: counter dict (commented) ---
" Verdict:     Correct. O(n) / O(n).
" Issues:
"   1. Pre-seed-then-count: `{num: 0 for num in nums}` then a second pass to
"      increment. Two O(n) passes when one suffices. Worse, the upfront
"      comprehension destroys the short-circuit benefit — see `dup-at-1`:
"      7.81ms vs optimal 0.36ms.
"   2. Counter is overkill for a presence question. A `set` answers
"      "have I seen this?" with less memory per slot and a simpler model.
"      Reach for Counter only when you need *how many*; reach for set when
"      you only need *whether*.
"
" --- Solution #2: len(set) != len(nums) (active) ---
" Verdict:     Correct. O(n) / O(n). Fastest on the no-dup case.
" Issues:
"   1. No early exit — `set(nums)` always consumes the whole iterator.
"      Wins on `distinct` (6.22ms, pure C) but loses badly on `dup-at-1`
"      (7.52ms vs 0.36ms for the explicit loop).
"   2. `if cond: return True else: return False` → `return cond`.
"      Most common Python antipattern interviewers flag.
"
" Recurring patterns flagged (see memory/user_recurring_patterns):
"   - Pre-seed-then-count (counter solution)
"   - `if cond: return True else: return False` stylistic noise (setlen)
"
" Interview takeaway: ship `seen = set(); ...` with the explicit loop.
" It shows you understand membership + early exit + how it generalizes to
" streams. The one-liner is fine for code golf when you know you'll always
" consume the input — mention the trade-off explicitly.
"""
