N = int(input())
PLANS = list( map(str, input().split()))

X, Y = 0, 0

move = { 'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

for plan in PLANS:

    X += move[plan][0]
    Y += move[plan][1]

    if X < 0 or Y < 0 or X >= N or Y >= N:
        X -= move[plan][0]
        Y -= move[plan][1]

print(X+1, Y+1)
