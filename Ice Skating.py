def bfs(snowdrifts, start, visited):
    queue = deque( [start] )

    while queue:
        v = queue.popleft()

        for i,coordinate in enumerate(snowdrifts):
            if visited[i]:
                continue

            if v[0] == coordinate[0] or v[1] == coordinate[1]:
                visited[i] = True
                queue.append(coordinate)

    return visited

from collections import deque

n = int(input())

snowdrifts = []
for i in range(n):
    snowdrift = tuple(map(int, input().split()))
    snowdrifts.append(snowdrift)

visited = [False] * n

graphs = []
for i in range(n):
    if visited[i]:
        continue

    visited[i] = True
    graphs.append(bfs(snowdrifts, snowdrifts[i], visited))

answer = len(graphs) - 1
print(answer)
