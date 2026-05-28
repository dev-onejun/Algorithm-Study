"""
" https://leetcode.com/problems/group-anagrams/
"
" Group strings that are anagrams of one another. Return the groups in any
" order; order within a group doesn't matter either.
"
" Constraints:
"   1 <= len(strs) <= 10^4          (N)
"   0 <= len(strs[i]) <= 100        (K)  -- note: "" is a valid string
"   strs[i] is lowercase English letters only.
"
" The whole problem is: pick a CANONICAL KEY that is identical for anagrams and
" distinct otherwise, then bucket by it. This is Valid Anagram lifted from a
" pairwise yes/no into a group-by -- there we compared two strings' letter
" counts; here we hash each string to its letter-count signature and collect
" the collisions. The two natural keys -- sorted(s) [O(K log K)] and the
" 26-count tuple [O(K)] -- mirror that file's Stage 1 (sort) vs Stage 3
" (fixed-size array) exactly.
"""

from collections import Counter, defaultdict
from typing import List


# ----- Stage 1: brute force, anagram-check vs each group -- O(N^2 * K) ------
# For each string, walk the existing groups and join the first whose
# representative is an anagram (compare letter counts); else open a new group.
# Rescanning every prior group for each string is the N^2 factor.
def group_anagrams_brute(strs: List[str]) -> List[List[str]]:
    groups: List[List[str]] = []
    reps: List[Counter] = []  # letter-count of each group's representative
    for s in strs:
        cs = Counter(s)
        for i, rep in enumerate(reps):
            if rep == cs:
                groups[i].append(s)
                break
        else:
            groups.append([s])
            reps.append(cs)
    return groups


# ----- Stage 2: bucket by sorted-string key -- O(N * K log K) time ----------
# sorted("eat") == sorted("tea") == "aet", so the sorted string is a canonical
# anagram key. Single dict pass; O(K log K) per string for the sort.
def group_anagrams_sorted(strs: List[str]) -> List[List[str]]:
    buckets: dict[str, List[str]] = defaultdict(list)
    for s in strs:
        buckets["".join(sorted(s))].append(s)
    return list(buckets.values())


# ----- Stage 3: bucket by 26-count tuple key -- O(N * K) time (optimum) -----
# Same idea, but the key is the letter-frequency vector built in one O(K) pass,
# dropping the log K sort factor. The tuple is hashable so it keys the dict
# directly. Same fixed 26-array trick as Valid Anagram Stage 3.
#
# CAVEAT (CPython constants): this only WINS for large K. The count loop runs
# char-by-char in Python, while Stage 2's sorted()/"".join() run in C. Measured
# N=10^4: K=10 -> sorted ~= count; K=50 -> count 1.5x faster; K=100 (the
# constraint ceiling) -> count 1.8x faster. Crossover ~K=10-20. Asymptotically
# optimal; for short strings Stage 2 is the pragmatic pick.
def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    buckets: dict[tuple, List[str]] = defaultdict(list)
    A = ord('a')
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - A] += 1
        buckets[tuple(counts)].append(s)
    return list(buckets.values())


# ----- User's submission (self stripped) -----------------------------------
# Sorted-key bucketing (the Stage 2 idea), but with an extra precompute pass:
# first build orig -> sorted(orig) into a dict, then re-iterate to bucket.
def group_anagrams_user(strs: List[str]) -> List[List[str]]:
    # Overall: O(n logn)
    sorted_strs: dict[str, str] = {orig: ''.join(sorted(orig)) for orig in strs}

    out_dict: dict[str, str] = {}
    for orig in strs:
        if sorted_strs[orig] in out_dict:
            out_dict[sorted_strs[orig]].append(orig)
        else:
            out_dict[sorted_strs[orig]] = [orig]
    return list(out_dict.values())


"""
" ============================================================================
" Review of submitted solution (`group_anagrams_user`) — 2026-05-28
" ============================================================================
"
" Verdict:     Correct. Passes all 8 cases (incl. duplicate-heavy
"              ["aa","aa","bb"] and ["ab","ab","ab","ba","ba"]) and agrees with
"              the 26-count reference on a 10^4 random stress. Right idea: the
"              sorted string as canonical anagram key — same as Stage 2.
" Asymptotic:  O(N * K log K) time, O(N * K) space. Matches Stage 2 / the
"              optimum class for K <= 100. The "# O(n logn)" comment is
"              imprecise: cost is N strings each sorted in K log K, not one
"              n log n.
" Stress:      N=10^4 K<=10: user 7.38ms vs single-pass Stage 2 5.77ms (~1.3x).
"              K=100: 115 vs 111ms (tie — the unavoidable sort dominates and
"              hides the overhead). all-duplicate 10^4: 68 vs 69ms (tie).
"
" Correctness note (the trap that ISN'T one):
"   - `{orig: ... for orig in strs}` collapses duplicate strings into a single
"     dict entry, but this does NOT lose data: the bucketing loop iterates the
"     full `strs` list, so every duplicate is still appended. Verified on the
"     duplicate cases. The natural worry here is real — good instinct to check.
"
" Issues (ordered by impact):
"   1. The `sorted_strs` precompute is PURE OVERHEAD — a two-pass solution where
"      one pass suffices. And the benefit you might expect from it (sort a
"      repeated string only once) DOES NOT EXIST: a dict comprehension evaluates
"      the value expr `''.join(sorted(orig))` for EVERY element regardless of key
"      collisions, so the sort still runs N times. The all-duplicate benchmark
"      (10^4 copies of one 100-char string) is break-even (68 vs 69ms) — proof
"      the extra dict buys nothing while costing a full pass + ~N*K memory.
"      Fold the sort inline into the single bucketing loop.
"   2. `out_dict: dict[str, str]` — the values are `list[str]`, not `str`. Python
"      skips local annotation eval so it runs fine, but mypy/pyright would flag
"      `.append` on a str-typed value. Same class as `dict[str, num]` in Valid
"      Anagram.
"   3. Manual `if key in d: d[key].append() else: d[key] = [...]` plus repeated
"      `sorted_strs[orig]` lookups (2-3 hash lookups of a length-K key per
"      iteration). `defaultdict(list)` (or `d.setdefault(k, []).append`) does it
"      in one and removes the precompute dict entirely.
"
" Canonical single-pass form (Stage 2):
"     buckets = defaultdict(list)
"     for s in strs:
"         buckets["".join(sorted(s))].append(s)
"     return list(buckets.values())
"
" Recurring patterns flagged (see memory/user_recurring_patterns):
"   - #1 variant: precompute-a-structure-then-re-iterate. Same two-pass shape as
"     the Valid Anagram pre-seed-then-count — build an auxiliary dict in one pass
"     to consume in the next, when a single pass does both.
"   - #5: wrong local type annotation silently accepted (`dict[str, str]` for a
"     list-valued dict). 2nd sighting after Valid Anagram's `dict[str, num]`.
"
" Optimum gap: asymptotically optimal (O(N*K log K), same as Stage 2). For
" K <= 100 this is the pragmatic pick; the 26-count key (Stage 3) is the
" asymptotic optimum that pulls ahead ~1.8x only as K -> 100. The idea is
" exactly right; the precompute pass leaks a ~1.3x constant at small K for zero
" benefit. Delete it and it's clean and optimal.
"""
