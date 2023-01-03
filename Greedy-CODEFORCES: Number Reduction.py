"""
" https://codeforces.com/problemset/problem/1765/N
" Delete from 9 to 0
    - making exceptions according to the problem conditions.
    - FAILED.
"""
t = int(input())

while t:
    x = list(input())
    k = int(input())

    for num in range(9, -1, -1):
        if k == 0:
            break

        while True:
            try:
                target = x.index(str(num))
            except:
                target = -1

            if target == 0 and x[1] == '0':
                try:
                    target = x.index(str(num), 2)
                except:
                    target = -1

            if target == -1 or k == 0:
                break

            x.pop(target)
            k -= 1

    result = ''
    for char in x:
        result += char
    print(result)

    t -= 1
