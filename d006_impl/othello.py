BOARD_SIZE = 8

SYM_PLAYER_1 = '@'
SYM_PLAYER_2 = 'O'

board = [['_' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def set_piece(board, y, x, player):
    if player == 0:
        board[y][x] = SYM_PLAYER_1
    elif player == 1:
        board[y][x] = SYM_PLAYER_2

    adjudicate(x, y, player)

def adjudicate(x, y, player):
    other = SYM_PLAYER_2 if player == 0 else SYM_PLAYER_1
    my = SYM_PLAYER_1 if player == 0 else SYM_PLAYER_2

    adjusicate_vertical(board, x, y, my, other)
    adjusicate_horizontal(board, x, y, my, other)
    adjusicate_diagonal(board, x, y, my, other)
    

def adjusicate_vertical(board, x, y, my, other):
    # 위, 아래
    if y < BOARD_SIZE - 2: # 아래 방향 탐색
        others_symbols = []
        captured = False
        for i in range(y + 1, BOARD_SIZE):
            if board[i][x] == other:
                others_symbols.append((i, x))
                captured = True
            elif board[i][x] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
    if y >= 2: # 위 방향 탐색
        others_symbols = []
        captured = False
        for i in range(y - 1, -1, -1):
            if board[i][x] == other:
                others_symbols.append((i, x))
                captured = True
            elif board[i][x] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break

def adjusicate_horizontal(board, x, y, my, other):
    # 좌, 우
    if x < BOARD_SIZE - 2: # 오른쪽 방향 탐색
        others_symbols = []
        captured = False
        for i in range(x + 1, BOARD_SIZE):
            if board[y][i] == other:
                others_symbols.append((y, i))
                captured = True
            elif board[y][i] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
    if x > 2: # 왼쪽 방향 탐색
        others_symbols = []
        captured = False
        for i in range(x - 1, -1, -1):
            if board[y][i] == other:
                others_symbols.append((y, i))
                captured = True
            elif board[y][i] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break

def adjusicate_diagonal(board, x, y, my, other):
# 대각선
    if x < BOARD_SIZE - 2 and y < BOARD_SIZE - 2: # 오른쪽 아래 대각선 탐색
        others_symbols = []
        captured = False
        i, j = y + 1, x + 1
        while i < BOARD_SIZE and j < BOARD_SIZE:
            if board[i][j] == other:
                others_symbols.append((i, j))
                captured = True
            elif board[i][j] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
            i += 1
            j += 1
    # 왼쪽 위
    if x >= 2 and y >= 2: # 왼쪽 위 대각선 탐색
        others_symbols = []
        captured = False
        i, j = y - 1, x - 1
        while i >= 0 and j >= 0:
            if board[i][j] == other:
                others_symbols.append((i, j))
                captured = True
            elif board[i][j] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
            i -= 1
            j -= 1
    # 오른쪽 위
    if x < BOARD_SIZE - 2 and y >= 2: # 오른쪽 위 대각선 탐색
        others_symbols = []
        captured = False
        i, j = y - 1, x + 1
        while i >= 0 and j < BOARD_SIZE:
            if board[i][j] == other:
                others_symbols.append((i, j))
                captured = True
            elif board[i][j] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
            i -= 1
            j += 1
    # 왼쪽 아래
    if x >= 2 and y < BOARD_SIZE - 2: # 왼쪽 아래 대각선 탐색
        others_symbols = []
        captured = False
        i, j = y + 1, x - 1
        while i < BOARD_SIZE and j >= 0:
            if board[i][j] == other:
                others_symbols.append((i, j))
                captured = True
            elif board[i][j] == my:
                if captured:
                    for oy, ox in others_symbols:
                        board[oy][ox] = my
                break
            else:
                captured = False
                break
            i += 1
            j -= 1

def print_board(board):
    for row in board:
        print("".join(map(str, row)))

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

for idx in range(len(data)):
    x, y = data[idx]
    set_piece(board, BOARD_SIZE - y - 1, x, idx % 2)

    sym = 'x'
    if idx % 2 == 0:
        sym = 'X'
    else:
        sym = 'O'
# print(f"==> {x}, {BOARD_SIZE - y - 1} / {sym}")
print_board(board)
# _ = input()