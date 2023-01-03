S = str(input())

answer = 0

for char in S:
    num = int(char)

    if 0 <= num <= 1 or 0 <= answer <= 1:
        answer += num
    else:
        answer *= num

print(answer)
