from collections import deque
from typing import List, Tuple

def dfs(graph: List[List[int]], v: Tuple, visited: List[bool]) -> int:
    idx: int = v[0]
    bribe: int = v[1]

    visited[idx] = True

    for i in graph[idx]:
        if not visited[i]:
            #dfs(graph, (i, c[i-1]), visited)
            return min(bribe, dfs(graph, (i, c[i]), visited) )

    return bribe

def bfs(graph, start: Tuple[int, int], visited):
    queue = deque([start])

    min_bribe = 1000000001
    while queue:
        v = queue.popleft()

        idx = v[0]
        bribe = v[1]

        visited[idx] = True
        min_bribe = min(min_bribe, bribe)

        for character in graph[idx]:
            if not visited[character]:
                queue.append( (character, c[character]) )

    return min_bribe

# n : the number of chracters in Overcity
# m : the number of pairs of friends
n, m = map(int, input().split())
c = list(map(int, input().split() ) )

#graph: List[List[int]] = [ [] ] * (n+1)
graph: List[List[int]] = [ [] for i in range(n+1) ]
for i in range(m):
    n1, n2 = map(int, input().split() )
    graph[n1].append(n2)
    graph[n2].append(n1)

c.insert(0, 0)
visited = [False] * len(c)
answer: int = 0
visited[0] = True
for idx, bribe in enumerate(c):
    if not visited[idx]:
        #answer += dfs(graph, (idx, bribe), visited)
        answer += bfs(graph, (idx, bribe), visited)

print(answer)
