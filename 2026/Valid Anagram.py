"""
" https://leetcode.com/problems/valid-anagram/
"
" Return True iff `t` is an anagram of `s`.
"
" Constraints:
"   1 <= len(s), len(t) <= 5 * 10^4
"   s and t consist of lowercase English letters.
"""

from collections import Counter
from typing import List  # noqa: F401  (kept for parity with other files)


# ----- Stage 1: sort both, compare -- O(n log n) time, O(n) space ----------
def is_anagram_sort(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


# ----- Stage 2: hash map / Counter -- O(n) time, O(k) space ----------------
def is_anagram_counter(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# ----- User submission (de-commented from docstring, `num` -> `int`) -------
def is_anagram_user(s: str, t: str) -> bool:
    s_dict_table: dict[str, int] = {char: 0 for char in s}
    t_dict_table: dict[str, int] = {char: 0 for char in t}

    for char in s:
        s_dict_table[char] += 1
    for char in t:
        t_dict_table[char] += 1

    return s_dict_table == t_dict_table


# ----- Stage 3: fixed-size 26-array -- O(n) time, O(1) space (optimum) -----
def is_anagram_array(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts = [0] * 26
    A = ord('a')
    for cs, ct in zip(s, t):
        counts[ord(cs) - A] += 1
        counts[ord(ct) - A] -= 1
    return all(c == 0 for c in counts)


"""
" ============================================================================
" Review of submitted solution (`is_anagram_user`) — 2026-05-25
" ============================================================================
"
" Verdict:     Correct after de-commenting. Passes all 10 test cases.
" Asymptotic:  O(n) time, O(k) space — matches optimum class.
" Stress:      9.96ms vs counter 4.55ms at n=50_000 (~2.2× slower).
"
" Two issues with the submission itself before the algorithm:
"   - The entire solution was inside a docstring; function returned None.
"     Always sanity-check that you de-commented before submitting.
"   - `dict[str, num]` annotation — `num` is not a type. Python silently
"     accepts this at runtime (local annotations aren't evaluated), but
"     mypy/pyright will fail it. Drop the annotation or use `dict[str, int]`.
"
" Algorithmic issues (ordered by impact):
"   1. Pre-seed-then-count, twice. Four full O(n) passes when one suffices.
"      The Stage 2 form `Counter(s) == Counter(t)` does it in one C-level
"      pass per string.
"   2. Two parallel structures (`s_dict_table` + `t_dict_table`) when one
"      counter with +1 for s / -1 for t suffices (Stage 3 trick). Halves
"      memory and merges into a single loop.
"   3. Missing length pre-check `if len(s) != len(t): return False`. Every
"      optimal anagram solution has this — costs O(1), saves an O(n) double
"      counting pass on the easy-reject case.
"
" Recurring patterns flagged (see memory/user_recurring_patterns):
"   - Pre-seed-then-count (now seen in 3 problems running)
"   - Parallel structures when one suffices
"   - Missing length pre-check
"
" Optimum gap: ~2.2× slower than Counter on stress; asymptotically optimal.
" Idea is right (count letters, compare counts); execution leaks constants.
"""
