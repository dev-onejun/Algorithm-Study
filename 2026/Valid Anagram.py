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
