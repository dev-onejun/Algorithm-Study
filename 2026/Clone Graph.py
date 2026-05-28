"""
" https://leetcode.com/problems/clone-graph/
"
" Given a reference to a node in a connected undirected graph, return a deep
" copy (clone): every node and edge duplicated into fresh objects, same
" structure, no object shared with the original.
"
" Constraints:
"   0 <= number of nodes <= 100        (V is SMALL)
"   1 <= Node.val <= 100, unique per node
"   No repeated edges, no self-loops. Graph is connected.
"
" THE crux is CYCLES, not depth. Every undirected edge is a 2-cycle (1<->2),
" so a naive recursive clone recurses 1->2->1->2->... forever. The fix is a map
" `original_node -> cloned_node` that does double duty:
"   (1) terminates on cycles  — a node already in the map returns its clone;
"   (2) preserves aliasing    — a node reachable by many paths is cloned ONCE,
"                               so the copy is a graph, not an exploded tree.
"
" NOTE: unlike Number of Islands (90_000) / Flood Fill (2_500), V <= 100 here,
" so recursive DFS depth <= 100 is well under CPython's ~1000 limit. Pattern #6
" (recursion-limit crash) does NOT apply — recursion is safe on this problem.
" Both correct stages are O(V + E) time, O(V) space.
"""

from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ----- Stage 1: naive recursion, NO map -- BROKEN (motivates the map) ------
# Clones a node then recursively clones each neighbor. On ANY cycle (i.e. any
# edge, since edges are undirected) it never terminates -> RecursionError.
# Shipped only to demonstrate why the clone-map is mandatory.
def clone_graph_naive_BROKEN(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    copy = Node(node.val)
    copy.neighbors = [clone_graph_naive_BROKEN(nb) for nb in node.neighbors]
    return copy


# ----- Stage 2: recursive DFS + clone-map -- O(V+E) time, O(V) space -------
# Register the clone in the map BEFORE recursing into neighbors, so a back-edge
# to an in-progress node finds the existing clone instead of looping.
def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    clones: dict[Node, Node] = {}

    def dfs(n: Node) -> Node:
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy                      # register BEFORE recursing
        for nb in n.neighbors:
            copy.neighbors.append(dfs(nb))
        return copy

    return dfs(node)


# ----- Stage 3: iterative BFS + clone-map -- O(V+E) time, O(V) space -------
# Same idea, explicit queue. Create a node's clone when first seen; wire each
# edge cur->nb by appending the (already-created) clone of nb.
def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    if node is None:
        return None
    clones: dict[Node, Node] = {node: Node(node.val)}
    q = deque([node])
    while q:
        cur = q.popleft()
        for nb in cur.neighbors:
            if nb not in clones:
                clones[nb] = Node(nb.val)     # first sighting -> make clone
                q.append(nb)
            clones[cur].neighbors.append(clones[nb])
    return clones[node]


# ----- User's submission (self stripped) -----------------------------------
# Recursive DFS + clone-map — identical in shape to Stage 2.
def cloneGraph_user(node: Optional[Node]) -> Optional[Node]:
    if node == None:
        return None

    clones: dict[Node, Node] = {}

    def _dfs(n: Node) -> Node:
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy
        for neighbor in n.neighbors:
            copy.neighbors.append(_dfs(neighbor))
        return copy

    return _dfs(node)


"""
" ============================================================================
" Review of submitted solution (`cloneGraph_user`) — 2026-05-27
" ============================================================================
"
" Verdict:     Correct and OPTIMAL — best submission in the set. Stage 2
"              reference essentially line-for-line. Passes all 6 cases, each
"              checked for structure + original-unmutated + true deep copy
"              (zero shared node objects).
" Asymptotic:  O(V + E) time, O(V) space (clone-map + recursion stack <= 100).
"              Matches optimum.
" Stress:      uninformative at V <= 100 (sub-ms) — same as Flood Fill.
"
" What's RIGHT (worth naming, since these are the load-bearing details):
"   - Registers `clones[n] = copy` BEFORE the neighbor loop -> a back-edge to an
"     in-progress node finds the existing clone. This is the exact line that
"     makes the 4-cycle in Example 1 terminate. Nailed it.
"   - `if node == None: return None` empty guard present (Example 3).
"   - Chose recursion, and it's the RIGHT call here: V <= 100 caps depth at 100,
"     well under CPython's ~1000. Pattern #6 (recursion-limit crash) does NOT
"     apply — the standing gap from Number of Islands / Flood Fill is absent
"     because the bound is small. Good judgment on when recursion is safe.
"
" Issues (the only one):
"   1. `node == None` -> `node is None`. Looks like PEP 8, but the substance is
"      real here: the clone-map is KEYED BY Node objects, which works only
"      because LeetCode's Node defines no __eq__/__hash__, so dict lookups use
"      object IDENTITY. That assumption is load-bearing — if Node had
"      value-equality (__eq__ by val), two distinct same-val nodes would COLLIDE
"      as dict keys and corrupt the clone, and `== None` would route through
"      __eq__. `is None` is a direct identity check: faster (no dispatch) and
"      immune to a custom __eq__. Use it to make the identity semantics the
"      algorithm already relies on explicit.
"
" Recurring patterns (see memory/user_recurring_patterns): NONE triggered.
" Notably the first graph problem where recursion was the right tool and was
" used cleanly — improvement over the NoI/Flood-Fill recursive-depth crashes.
"
" Optimum gap: none. Asymptotically and constructively optimal; identical to
" the reference DFS. Only the `== None` -> `is None` micro-edit.
"""
