"""
" https://leetcode.com/problems/flood-fill/
"
" Given an m x n grid `image` and a start pixel (sr, sc), recolor the start
" pixel and every pixel 4-directionally connected to it THROUGH pixels of the
" start pixel's original color, setting them all to `color`. Return the image.
"
" Constraints:
"   m == len(image), n == len(image[0])
"   1 <= m, n <= 50            (up to 2_500 cells)
"   0 <= image[i][j], color < 2**16
"   0 <= sr < m, 0 <= sc < n
"
" THE trap: if the start pixel ALREADY equals `color`, a naive fill keeps
" 'recoloring' same-colored cells, so the "matches original" test never
" excludes them -> infinite recursion. Guard with `if original == color:
" return image` up front. This is the flood-fill kernel that Number of Islands
" runs internally; both share the recursion-depth caveat (pattern #6).
"
" Both stages are Theta(region) time, O(m*n) worst case. The progression here
" is depth-safety (recursion -> explicit frontier), not asymptotics.
"""

from collections import deque
from typing import List


# ----- Stage 1: recursive DFS, in place ------------------------------------
# O(region) time, O(region) recursion stack. Simplest; but a fully-connected
# 50x50 region recurses ~2500 deep -> past CPython's ~1000 limit (see Stage 2).
def flood_fill_dfs(image: List[List[int]], sr: int, sc: int,
                   color: int) -> List[List[int]]:
    original = image[sr][sc]
    if original == color:                 # critical: else infinite recursion
        return image
    m, n = len(image), len(image[0])

    def fill(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original:
            return
        image[r][c] = color               # color != original -> won't revisit
        fill(r + 1, c)
        fill(r - 1, c)
        fill(r, c + 1)
        fill(r, c - 1)

    fill(sr, sc)
    return image


# ----- Stage 2: iterative BFS, explicit queue ------------------------------
# O(region) time, O(region) frontier, but NO recursion-depth risk -> the
# depth-safe default. Recolor on ENQUEUE so a cell is never queued twice.
def flood_fill_bfs(image: List[List[int]], sr: int, sc: int,
                   color: int) -> List[List[int]]:
    original = image[sr][sc]
    if original == color:
        return image
    m, n = len(image), len(image[0])
    image[sr][sc] = color
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                image[nr][nc] = color     # recolor on enqueue
                q.append((nr, nc))
    return image


# ----- User's submission (self stripped) -----------------------------------
# Recursive DFS with a separate `visited` matrix — handles the equal-color
# case STRUCTURALLY (visited blocks re-processing) instead of via a
# `target == color` early-return guard.
def floodFill_user(image: List[List[int]], sr: int, sc: int,
                   color: int) -> List[List[int]]:
    M, N = len(image), len(image[0])
    visited = [[False for _ in range(N)] for _ in range(M)]

    def dfs(m: int, n: int) -> None:
        if m < 0 or n < 0 or m >= M or n >= N:
            return
        if visited[m][n]:
            return
        visited[m][n] = True
        if image[m][n] == target:
            image[m][n] = color
            dfs(m + 1, n)
            dfs(m, n + 1)
            dfs(m - 1, n)
            dfs(m, n - 1)
        else:
            return
        return

    target = image[sr][sc]
    dfs(sr, sc)
    return image


"""
" ============================================================================
" Review of submitted solution (`floodFill_user`) — 2026-05-27
" ============================================================================
"
" Verdict:     Correct on all 8 cases, and it SIDESTEPS the equal-color trap —
"              the `visited` matrix marks a cell even when the recolor is a
"              no-op, so Example 2 terminates instead of looping. Solved
"              structurally rather than with the `target == color` guard. But
"              RecursionError on a 50x50 all-same region (a legal input).
" Asymptotic:  O(m*n) time (optimal class). O(m*n) space — `visited` matrix
"              PLUS recursion stack.
" Stress:      uninformative at n<=50 (a 'big' region is 2_500 cells, sub-ms) —
"              but that same region overflows the recursive stack, which IS the
"              signal here.
"
" Issues (ordered by impact):
"   1. Recursion-depth crash — pattern #6, now seen TWICE (Number of Islands,
"      Flood Fill). Identical recursive structure, identical liability: depth =
"      region size, ~2500 on a full 50x50 grid > CPython's ~1000 limit. This is
"      now a trend, not a one-off. Fix: iterative BFS (Stage 2) — same O(m*n),
"      no stack. NOT sys.setrecursionlimit (segfault risk).
"   2. Equal-color handled, but the slow way. The `visited` matrix makes
"      Example 2 correct, yet still traverses the WHOLE region recoloring
"      same->same. The early guard `if target == color: return image` is O(1)
"      instead of O(region), AND lets you drop `visited` entirely (O(m*n)->O(1)
"      extra space) — once color != target, a recolored cell can't re-match, so
"      the color change itself is the visited-marker (Stages 1/2 rely on this).
"      Two valid designs: {guard, no visited, O(1)} vs {visited, no guard,
"      O(m*n)}. Yours is robust-by-construction but pays space + redundant work.
"   3. Redundant control flow (pattern #5 family). The tail is dead weight:
"          if image[m][n] == target:
"              image[m][n] = color
"              dfs(...) x4
"          else:
"              return          # no-op
"          return              # no-op; returns None either way
"      Guard-clause inversion flattens it: `if image[m][n] != target: return`,
"      then recolor + recurse, no else.
"   4. Nit: `target` is assigned AFTER the nested `dfs` that closes over it.
"      Works (late binding; the call runs after assignment), but define `target`
"      before `dfs` to read top-to-bottom.
"
" Recurring patterns (see memory/user_recurring_patterns):
"   - #6 recursive-DFS stack-limit crash — now confirmed across BOTH graph
"     problems. The reflex to reach for recursion on grids is the standing gap.
"   - #5 redundant `if/else: return` + trailing return — mild instance here.
"
" Optimum gap: idea is optimal (O(m*n) flood fill) and the equal-color handling
" is correct. The recursive form is disqualified on a large region by the stack
" limit — the SAME gap as Number of Islands, fixed the same mechanical way
" (explicit frontier). Secondary: visited-without-guard costs O(m*n) space and
" an O(region) no-op pass on the equal-color case vs. the O(1) guard.
"""
