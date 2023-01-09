N = int(input())

answer = 0
for hours in range(N+1):
    for miniutes in range(60):
        for seconds in range(60):
            hour = str(hours)
            miniute = str(miniutes)
            second = str(seconds)

            target = hour + miniute + second
            if target.count('3'):
                answer += 1

print(answer)
