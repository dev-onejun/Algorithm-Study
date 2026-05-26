"""
" https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"
" Given a 1-indexed array `numbers` sorted in non-decreasing order, return the
" 1-based indices [index1, index2] (index1 < index2) of the two values that
" sum to `target`. Exactly one solution exists; no element reused.
"
" MUST use only constant extra space.
"
" Constraints:
"   2 <= len(numbers) <= 3 * 10^4
"   -1000 <= numbers[i], target <= 1000
"   numbers is sorted non-decreasing; exactly one solution.
"
" Note: the O(n)-space hash-map trick from the original Two Sum is DISALLOWED
" here by the constant-space rule. That rule is the whole point of the sorted
" variant — sortedness is what lets you find the pair without a hash map.
"""

from typing import List


# ----- Stage 1: brute force -- O(n^2) time, O(1) space ---------------------
def two_sum_brute(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


# ----- Stage 2: binary-search the complement -- O(n log n) time, O(1) space-
# Insight: the array is sorted, so for each i the complement (target-nums[i])
# can be found by binary search instead of a linear inner loop.
def two_sum_bisect(numbers: List[int], target: int) -> List[int]:
    import bisect
    n = len(numbers)
    for i in range(n):
        need = target - numbers[i]
        lo = bisect.bisect_left(numbers, need, i + 1)
        if lo < n and numbers[lo] == need:
            return [i + 1, lo + 1]
    return []


# ----- Stage 3: two pointers from both ends -- O(n) time, O(1) space (opt) -
# Insight: start wide. If the sum is too big the largest element can't be in
# the answer -> move the right pointer in; if too small, move left in. Each
# step eliminates one element, so it's a single O(n) pass with no extra space.
def two_sum_twoptr(numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i + 1, j + 1]
        elif s < target:
            i += 1
        else:
            j -= 1
    return []


# ----- User's submission (self stripped; dead brute-force docstring kept) ---
def twoSum_user(numbers: List[int], target: int) -> List[int]:
    """ Overall: O(n^2) -- Time limit exceeded
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            candidate = numbers[i] + numbers[j]
            if candidate == target:
                if i == j:
                    continue
                return i + 1, j + 1
            elif candidate > target:
                break
    """
    ptr1, ptr2 = 0, len(numbers) - 1
    cand_sum = numbers[ptr1] + numbers[ptr2]

    while cand_sum != target:
        if cand_sum > target:
            ptr2 -= 1
        elif cand_sum < target:
            ptr1 += 1

        cand_sum = numbers[ptr1] + numbers[ptr2]

    return [ptr1 + 1, ptr2 + 1]


"""
" ============================================================================
" Review of submitted solution (`twoSum_user`) — 2026-05-26
" ============================================================================
"
" Verdict:     Correct. Passes all 10 test cases.
" Asymptotic:  O(n) time, O(1) space — matches optimum, and satisfies the
"              constant-space requirement (no hash map).
" Stress:      2.18 ms vs reference two-pointer 2.19 ms at n=3*10^4.
"              Dead even — first submission with NO measurable constant-factor
"              gap to optimum. The recurring index-loop / try-except / pre-seed
"              habits are all absent here. This is the right tool, applied well.
"
" Issues (minor, ordered by impact):
"   1. Loop guard relies on the problem's solution guarantee. `while cand_sum
"      != target` walks the pointers forever if no pair exists — verified it
"      throws IndexError on an off-spec no-solution input ([1,2,3], 100).
"      Fine for LeetCode, fragile in general; interviewers like to ask "what
"      if there's no solution?". The robust idiom guards on the pointers:
"          while ptr1 < ptr2:
"              s = numbers[ptr1] + numbers[ptr2]
"              if s == target: return [ptr1+1, ptr2+1]
"              elif s < target: ptr1 += 1
"              else: ptr2 -= 1
"   2. Duplicated sum line. `cand_sum = numbers[ptr1] + numbers[ptr2]` appears
"      twice — once to seed before the loop, once at the loop tail. The
"      `while ptr1 < ptr2` form above computes it once as the first line of
"      the body, deleting the seed line. Zero perf difference; pure dedupe.
"   3. `elif cand_sum < target` can be a bare `else`: inside the loop the sum
"      is guaranteed != target, so `<` is the only remaining case. Tiny.
"   4. Dead brute force (commented): `for j in range(i, len)` + `if i == j:
"      continue` is cleaner as `range(i + 1, len)` with no self-check. Good
"      instinct on the `break` when candidate > target — that uses sortedness
"      to early-terminate, better than a naive O(n^2).
"
" Recurring patterns: none of the usual ones triggered this round (see
" memory/user_recurring_patterns). Notable improvement.
"
" Optimum gap: none measurable. Asymptotically and constant-factor optimal.
"""
