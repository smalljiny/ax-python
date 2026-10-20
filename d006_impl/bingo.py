bingo_board_size = 5

def mark_score_board(score_board):
    bingo_horizontal = [0] * bingo_board_size
    bingo_vertical = [0] * bingo_board_size
    bingo_cross = [0] * 2

    bingo_count = 0

    for idx in range(bingo_board_size):
        for jdx in range(bingo_board_size):
            bingo_horizontal[idx] += score_board[idx][jdx]
            if bingo_horizontal[idx] == bingo_board_size:
                bingo_count += 1

            bingo_vertical[jdx] += score_board[idx][jdx]
            if bingo_vertical[jdx] == bingo_board_size:
                bingo_count += 1

            if idx == jdx:
                bingo_cross[0] += score_board[idx][jdx]
                if bingo_cross[0] == bingo_board_size:
                    bingo_count += 1

            if idx + jdx == bingo_board_size - 1:
                bingo_cross[1] += score_board[idx][jdx]
                if bingo_cross[1] == bingo_board_size:
                    bingo_count += 1
    return bingo_count >= 3

user_board = {}
score_board = [[0] * bingo_board_size for _ in range(bingo_board_size)]

for idx in range(bingo_board_size):
    row = list(map(int, input().split()))
    for jdx in range(bingo_board_size):
        user_board[row[jdx]] = (idx, jdx)

draw_board = []

for _ in range(bingo_board_size):
    draw_board.append(list(map(int, input().split())))

bingo_num = 0

def print_score_board(score_board):
    for row in score_board:
        print(" ".join(map(str, row)))

for row in draw_board:
    for num in row:
        x, y = user_board[num]
        score_board[x][y] = 1
        if mark_score_board(score_board):
            bingo_num = num
            break
    if bingo_num:
        break

print(bingo_num)
