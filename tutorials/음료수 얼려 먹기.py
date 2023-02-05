N, M = map(int, input().split())

ice_tray = []

for i in range(N):
    string = input()

    row = []
    for j in string:
        row.append(int(j))

    ice_tray.append(row)

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def bfs(ice_tray, start, visited):
    queue = deque([start])

    if visited[start[0]][start[1]]:
        return 0

    visited[start[0]][start[1]] = True

    while queue:
        v = queue.popleft()

        for d in zip(dx, dy):
            if not visited[d[0]][d[1]] and not ice_tray[d[0]][d[1]]:
                queue.append([d])
                visited[d[0]][d[1]] = True

    return 1

visited = [ [False]*M ]*N

for i in range(N):
    for j in range(M):
        answer += bfs(ice_tray, (i, j), visited)

print(answer)
