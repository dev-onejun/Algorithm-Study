from collections import deque

def bfs(maps, start, visited):
    queue = deque([start])
    count = None

    visited[start[0]][start[1]] = True
    while queue:
        v = queue.popleft()

        if (v[0], v[1]) == (N - 1, M - 1):
            count = v[2]
            break

        try:
            if not visited[v[0] + 1][v[1]]:
                queue.append( (v[0] + 1, v[1], v[2]+1) )
                visited[v[0]+1][v[1]] = False
            if not visited[v[0] - 1][v[1]]:
                queue.append( (v[0] - 1, v[1], v[2]+1) )
                visited[v[0]-1][v[1]] = False
            if not visited[v[0]][v[1] + 1]:
                queue.append( (v[0], v[1] + 1, v[2]+1) )
                visited[v[0]][v[1]+1] = False
            if not visited[v[0]][v[1] - 1]:
                queue.append( (v[0], v[1] - 1, v[2]+1) )
                visited[v[0]][v[1]-1] = False
        except IndexError:
            pass

    return count


N, M = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(map(int, input())))

visited = list(maps)
visited = [ [1 if x == 0 else 0 for x in row] for row in maps]

# start = (row, col, move_conut)
answer = bfs(maps, (0,0,1), visited)
print(answer)
