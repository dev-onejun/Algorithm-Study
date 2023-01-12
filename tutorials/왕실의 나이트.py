INIT_POS = input()

MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
ONE_TO_ONE = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

ROW = int(INIT_POS[1])
COL = ONE_TO_ONE[INIT_POS[0]]

answer = 0
for move in MOVES:
    if ROW + move[0] < 1 or ROW + move[0] > 8 or COL + move[1] < 1 or COL + move[1] > 8:
        continue

    answer += 1

print(answer)
