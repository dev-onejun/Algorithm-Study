from typing import List, Tuple
import sys
sys.setrecursionlimit(10**7)

def dfs(v: Tuple, visited: List[bool]) -> int:
    idx: int = v[0]
    bribe: int = v[1]

    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs((i, c[i-1]), visited)

    return bribe

# n : the number of chracters in Overcity
# m : the number of pairs of friends
n, m = map(int, input().split())
c = list(map(int, input().split() ) )
print(c)

#graph: List[List[int]] = [ [] ] * (n+1)
graph: List[List[int]] = [ [] for i in range(n+1) ]
for i in range(m):
    n1, n2 = map(int, input().split() )
    graph[n1].append(n2)
    graph[n2].append(n1)
print(graph)

characters: List[Tuple] = [] # (index, bribe)
for idx, bribe in enumerate(c):
    characters.append( (idx + 1, bribe) )
characters.sort(key=lambda character: character[1]) # sort by bribe
print(characters)

visited = [False] * (len(c) + 1)
visited[0] = True
answer: int = 0
for character in characters:
    if not visited[character[0]]:
        answer += dfs(character, visited)

print(answer)
