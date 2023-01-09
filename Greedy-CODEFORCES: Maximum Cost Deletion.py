"""
" https://codeforces.com/problemset/problem/1550/B

" Delete the maximum possible length of substring if a is larger than (or equal to) 0.
"" if a is smaller than 0, just delete one by one characters.

" the given formula, a * l + b, can convert to a*n + b*k.
"" Furthermore, when the string s is splited to the m blocks,
    "" floor(m/2)+1 is the minimum number of operations

"""

import math

t = int(input())

for testcase in range(t):
    n, a, b = map(int, input().split())
    s = input()

    score = 0

    if b >= 0:
        for i in range(n):
            score += 1 * a + b

    else:
        m = 0
        for i,char in enumerate(s):
            try:
                if char != s[i-1]:
                    m += 1
            except:
                continue

        k = math.floor(m/2) + 1
        score = a * n + b * k

    print(score)

