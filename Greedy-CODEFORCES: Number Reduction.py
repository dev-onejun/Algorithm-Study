"""
" https://codeforces.com/problemset/problem/1765/N

" Delete from 9 to 0
    - making exceptions according to the problem conditions.
    - FAILED.

" Delete the maximum number in X[:k+1]
    - the key idea to make the minimum positive integer is just descending the number of digits.
    - and the possible digit to remove is only in the range of 0 ~ k.

    - continuously WA on test 2
"""
t = int(input())

answer = []

while t:
    x = list(input().lstrip('0'))
    k = int(input())

    n = len(x)
    for i in range(k):
        if n <= 1:
            break

        target = max(x[:n - k])

        if x.index(target) == 0 and x[1] == '0':
            target = max(x[1: n-k+1])

        x.remove(target)

    result = ''.join(x)
    answer.append(result)

    t -= 1

for output in answer:
    print(output)
