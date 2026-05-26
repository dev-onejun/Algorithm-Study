"""
" https://leetcode.com/problems/valid-palindrome/
"
" A phrase is a palindrome if, after lowercasing and dropping every
" non-alphanumeric character, it reads the same forward and backward.
" Return True iff `s` is such a palindrome.
"
" Constraints:
"   1 <= len(s) <= 2 * 10^5
"   s consists only of printable ASCII characters.
"""

from typing import List  # noqa: F401  (kept for parity with other files)


# ----- Stage 1: clean into a string, compare with its reverse --------------
# O(n) time, O(n) space
def is_palindrome_clean(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]


# ----- Stage 2: clean once, two pointers over the cleaned list -------------
# O(n) time, O(n) space — avoids building the reversed copy
def is_palindrome_clean_twoptr(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True


# ----- Stage 3: two pointers in place, skip non-alphanumeric ---------------
# O(n) time, O(1) space (optimum space; see note on CPython constants below)
def is_palindrome_inplace(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


# ----- User's submission (self stripped) -----------------------------------
def isPalindrome_user(s: str) -> bool:
    p_s = []
    for c in s:
        if c.isalpha() or c.isdecimal():
            p_s.append(c.lower())

    p_s = ''.join(p_s)
    rev_s = ''.join([p_s[i] for i in range(len(p_s) - 1, -1, -1)])

    return p_s == rev_s


"""
" Notes — 2026-05-26
"   Stages 1/2 are O(n) space because they materialize the cleaned chars;
"   Stage 3 is the textbook O(1)-space answer. In CPython, though, Stage 3 is
"   marginally SLOWER on wall-clock (~22 ms vs ~19 ms at n=2*10^5) because the
"   per-char `.isalnum()` / `.lower()` calls run in Python bytecode, while the
"   Stage 1/2 comprehension + slice run in C. So Stage 3 wins on space and on
"   asymptotics, but the "optimal" label is space-only here, not speed.
"""


"""
" ============================================================================
" Review of submitted solution (`isPalindrome_user`) — 2026-05-26
" ============================================================================
"
" Verdict:     Correct. Passes all 14 test cases.
" Asymptotic:  O(n) time, O(n) space — matches optimum class.
" Stress:      ~21.5 ms vs Stage-1 reverse-slice ~15.0 ms at n=2*10^5
"              (~1.45x slower), almost entirely from the manual reverse loop.
"
" Issues (ordered by impact):
"   1. Manual reverse via index loop:
"        ''.join([p_s[i] for i in range(len(p_s)-1, -1, -1)])
"      This is the recurring `for i in range(len): xs[i]` indexing pattern
"      (see memory/user_recurring_patterns #5). `p_s[::-1]` is identical,
"      runs in C, and is one readable token. This loop is the whole ~1.45x gap.
"   2. Redundant join + second string. You already hold the cleaned chars in
"      the list `p_s` BEFORE joining. Compare the list to its own reverse:
"        return p_s == p_s[::-1]
"      No `''.join`, no separate `rev_s` — drops two O(n) allocations. (This
"      is exactly Stage 1.)
"   3. Reverse-and-compare always does full O(n) work, even when the mismatch
"      is at index 0. A two-pointer scan bails on the first mismatch (early
"      exit on non-palindromes) and the in-place form is O(1) space (Stage 3).
"      Same asymptotics, strictly less work on the reject path.
"   4. `c.isalpha() or c.isdecimal()` — correct, and under ASCII input it is
"      precisely [A-Za-z0-9]. `c.isalnum()` is the idiomatic shorthand and is
"      equivalent here (they diverge only on exotic Unicode numerics like
"      '²', which can't appear in printable-ASCII input). Style, not a bug.
"
" Recurring patterns flagged (see memory/user_recurring_patterns):
"   - `for i in range(len): xs[i]` indexing instead of slicing — now seen in
"     Two Sum and here. The canonical fix is `[::-1]` / slicing / enumerate.
"
" Optimum gap: ~1.45x slower than reverse-slice on stress; asymptotically
" optimal. The shape is right (clean -> compare to reverse); the constant
" factor leaks through reimplementing `[::-1]` and `str.join` by hand.
"""
