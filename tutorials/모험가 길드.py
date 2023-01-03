# 공포도 오름차순 sort, 그룹 만들기

N = int(input())
fears = list(map(int, input().split()))

fears.sort()

answer = 0
group = []
for fear in fears:
    group.append(fear)

    if len(group) >= fear:
        answer += 1
        group.clear()

print(answer)
