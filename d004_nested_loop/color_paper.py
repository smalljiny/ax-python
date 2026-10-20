N = int(input())
BOARD_SIZE = 1000
board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

counter = {}
for idx in range(1, N + 1):
    counter[idx] = 0

    (x, y, w, h) = map(int, input().split())

    for i in range(x, x + w):
        for j in range(y, y + h):
            board[i][j] = idx

for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] == 0:
            continue
        if board[i][j] in counter:
            counter[board[i][j]] += 1

for idx in range(1, N + 1):
    print(counter[idx])