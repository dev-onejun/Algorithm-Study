"""
" https://leetcode.com/problems/number-of-islands/
"
" Given an m x n grid of '1' (land) and '0' (water), return the number of
" islands. An island is a maximal set of land cells connected 4-directionally
" (up/down/left/right — NOT diagonally). All grid edges border water.
"
" Constraints:
"   m == len(grid), n == len(grid[0])
"   1 <= m, n <= 300            (so up to 90_000 cells)
"   grid[i][j] is '0' or '1'.
"
" Note: every correct solution is Theta(m*n) time — you must inspect each cell
" at least once, and connectivity needs at most one visit per cell. So the
" 'stages' below are NOT asymptotic speedups; they trade off recursion-depth
" safety, input mutation, and fitness for the dynamic follow-up (LC 305).
"""

from collections import deque
from typing import List


# ----- Stage 1: recursive DFS flood fill, sink in place --------------------
# O(m*n) time, O(m*n) space (recursion stack = size of the largest island).
# Simplest to write, but the stack depth can reach m*n on a fully-connected
# grid -> RecursionError (CPython default limit ~1000). See Stage 2.
# Mutates `grid` (sinks visited land to '0').
def num_islands_dfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '0'                      # mark visited by sinking
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1                    # new island found...
                sink(r, c)                    # ...drown the rest of it
    return count


# ----- Stage 2: iterative BFS flood fill, explicit queue -------------------
# O(m*n) time, O(min(m, n)) frontier in the typical case (O(m*n) worst case),
# but NO recursion-depth risk -> the interview-safe default.
# Subtlety: mark a cell '0' on ENQUEUE, not on dequeue, so the same cell is
# never queued twice (otherwise the queue can balloon to O(m*n*4)).
# Mutates `grid`.
def num_islands_bfs(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] != '1':
                continue
            count += 1
            grid[r][c] = '0'
            q = deque([(r, c)])
            while q:
                cr, cc = q.popleft()
                for nr, nc in ((cr + 1, cc), (cr - 1, cc),
                               (cr, cc + 1), (cr, cc - 1)):
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'    # mark on enqueue
                        q.append((nr, nc))
    return count


# ----- Stage 3: Union-Find (DSU) -- O(m*n * alpha) time, O(m*n) space ------
# Not faster than flood fill, but (a) does NOT mutate the grid and (b) is the
# canonical structure for the dynamic follow-up "Number of Islands II" (LC 305,
# cells added online): flood fill would re-scan O(m*n) per add, DSU merges in
# near-constant amortized time. Start with one component per land cell; every
# successful union of adjacent land merges two components into one.
def num_islands_dsu(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    parent = list(range(m * n))
    rank = [0] * (m * n)
    count = sum(row.count('1') for row in grid)

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]     # path halving
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        nonlocal count
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        count -= 1                            # two islands became one

    for r in range(m):
        for c in range(n):
            if grid[r][c] != '1':
                continue
            if r + 1 < m and grid[r + 1][c] == '1':   # only down + right;
                union(r * n + c, (r + 1) * n + c)       # up/left are symmetric
            if c + 1 < n and grid[r][c + 1] == '1':
                union(r * n + c, r * n + c + 1)
    return count


# ----- User's submission (self stripped) -----------------------------------
# Recursive DFS with a separate `traversed` visited matrix (preserves grid).
def numIslands_user(grid: List[List[str]]) -> int:
    M, N = len(grid), len(grid[0])
    traversed = [[False for _ in range(N)] for _ in range(M)]

    def dfs(m: int, n: int) -> bool:
        """
        Return
        ------
        True: Land
        False: Water
        """
        if m < 0 or n >= N or m >= M or n < 0:    # Water (Out of Index)
            return False
        if traversed[m][n]:                        # Already visited
            return False

        traversed[m][n] = True
        if grid[m][n] == "1":
            dfs(m + 1, n)
            dfs(m, n + 1)
            dfs(m - 1, n)
            dfs(m, n - 1)
            return True
        else:
            return False

    result = 0
    for m in range(M):
        for n in range(N):
            if dfs(m, n):
                result += 1
    return result


"""
" ============================================================================
" Review of submitted solution (`numIslands_user`) — 2026-05-27
" ============================================================================
"
" Verdict:     Correct on all 9 shape cases, but RAISES RecursionError on large
"              connected grids — a 100x100 all-land grid already dies, and the
"              300x300 all-land case (a legal input under the constraints)
"              definitely does. This is the canonical LeetCode-Python trap for
"              this problem, not a synthetic edge case.
" Asymptotic:  O(m*n) time (optimal class). O(m*n) space — a `traversed` matrix
"              PLUS the recursion stack (depth = largest island).
" Stress:      43.93 ms vs reference dfs 25.86 / bfs 29.32 / dsu 25.71 ms on the
"              300x300 vertical-stripe grid (~1.7x the in-place dfs). Stripes are
"              the only big grid that stays under the stack limit to be timed.
"
" Issues (ordered by impact):
"   1. Recursion-depth crash (headline). Recursive flood fill makes stack depth
"      = island size; at the 300x300 bound that's up to 90_000 frames, far past
"      CPython's ~1000 default. Identical liability to the reference Stage 1.
"      Fix is mechanical and asymptotically free: explicit stack/queue (Stage 2,
"      iterative BFS). NOTE sys.setrecursionlimit(10**6) is NOT a fix — it swaps
"      a clean RecursionError for a C-stack SEGFAULT.
"   2. Overloaded return / misleading docstring. The docstring says True=Land,
"      False=Water, but the function returns False for VISITED land too. What it
"      actually returns is "is (m,n) the seed of a freshly-discovered island?".
"      It works only because (a) the recursive calls discard the return and
"      (b) the outer loop's True-test coincides with "new seed" (an unvisited
"      land cell can only be a new island's seed). Rename to `started_new_island`
"      and fix the docstring — current naming is a foot-gun for the next reader.
"   3. A function call per cell (this is the measured ~1.7x). The outer loop
"      calls dfs on ALL m*n cells — water and already-visited included — each a
"      full Python call that does bounds+visited work only to return False.
"      Inline the guard and call the flood helper only on real seeds:
"          for m in range(M):
"              for n in range(N):
"                  if grid[m][n] == "1" and not traversed[m][n]:
"                      flood(m, n)          # side-effect only, no return
"                      result += 1
"      That deletes ~m*n calls. The helper also recurses into water neighbors
"      unconditionally (4 calls per land cell) — guarding before the call trims
"      more. Pure constant-factor; the asymptotics are already optimal.
"   4. Visited matrix vs in-place sink — neutral, arguably a plus. Keeping
"      `traversed` separate PRESERVES the input grid; a defensible space-for-
"      purity trade, not a bug. If mutation is allowed, sinking '1'->'0' drops
"      the O(m*n) matrix (reference Stages 1/2 do this).
"   5. No empty-grid guard: grid[0] IndexErrors on []. Moot under the m,n >= 1
"      constraints; `if not grid or not grid[0]: return 0` is the robust idiom.
"   6. Bounds check `m < 0 or n >= N or m >= M or n < 0` is correct but
"      interleaves m/n; `m < 0 or m >= M or n < 0 or n >= N` reads cleaner.
"
" Recurring patterns (see memory/user_recurring_patterns): none of #1–#5
" triggered (clean, like Two Sum II). But this is the first graph/DFS problem
" and it surfaces a NEW pattern — recursive DFS ignoring CPython's ~1000 stack
" limit on large bounded grids/graphs — logged as pattern #6 to watch on future
" tree/graph problems.
"
" Optimum gap: the IDEA is optimal (O(m*n) flood fill). But the recursive form
" is DISQUALIFIED on large connected inputs by a hard crash, not a slowdown. The
" mechanical fix (explicit frontier) keeps the complexity and removes the crash;
" on depth-safe inputs it still trails the in-place dfs ~1.7x on per-cell call
" overhead. Reach for iterative BFS (Stage 2) as the default here.
"""
