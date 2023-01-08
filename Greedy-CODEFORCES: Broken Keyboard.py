"""
" https://codeforces.com/problemset/problem/1765/B

" DFA that determines whether the number is dividened by 3 or not.

"""

t = int(input())
while t:
    n = int(input())
    s = input()

    if n % 3 == 2:
        print('NO')
        t -= 1
        continue

    answer = 'YES'
    for i in range(0, n, 3):
        if i+2 < n and s[i+1] != s[i+2]:
            answer = 'NO'
            break
    print(answer)

    t -= 1
