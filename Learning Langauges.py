from typing import List
from collections import deque

def bfs(employees: List[List[int]], start: int):
    global answer

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for language in employees[v]:
            for i in range(len(employees)):
                if visited[i]:
                    continue

                if employees[i].count(language):
                    visited[i] = True
                    queue.append(i)

    if visited.count(False):
        idx = visited.index(False)
        bfs(employees, idx)
        answer += 1

    return

n, m = map(int, input().split())

visited = [False] * n
answer = 0

employees: List[List[int]] = []
for i in range(n):
    employee = list( map( int, input().split()))

    # check whether the employee's language list is zero.
    if employee[0] == 0:
        visited[i] = True

    employee = employee[1:len(employee)]
    employees.append(employee)

# the corner case which all employees don't know any languages
if not visited.count(False):
    answer = len(employees)
else:
    visited.clear()
    visited = [False] * n
    bfs(employees, 0)

print(answer)
