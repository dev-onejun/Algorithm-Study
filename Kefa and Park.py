from typing import List, Tuple

def dfs(start: Tuple[int, int]) -> int:
    from collections import deque

    count: int = 0

    stack = deque( [start] )

    while stack:
        v = stack.pop()

        idx = v[0]
        cats = 0 if a[idx - 1] == 0 else v[1] + a[idx - 1]

        visited[idx] = True

        if cats > m:
            continue

        leaf = True
        for i in graph[idx]:
            if not visited[i]:
                stack.append((i, cats))
                leaf = False

        if leaf:
            count += 1

    return count


n, m = map(int, input().split() )

a = list(map( int, input().split() ) )

graph: List[List[int]] = [ [] for i in range(n+1) ]
for i in range(n-1):
    edge = tuple(map(int, input().split() ) )

    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = [False] * (n+1)
answer = dfs((1,0))
print(answer)
