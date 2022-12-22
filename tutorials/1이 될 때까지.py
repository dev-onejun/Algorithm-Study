N, K = map( int, input().split() )

result = 0
while N != 1 :
    result += 1

    # N이 K로 나누어 떨어질 때
    if N % K == 0:
        # 1번 연산
        N /= K
        continue

    # 2번 연산
    N -= 1

print(result)
