N = int(input(""))

cube = []

for _ in range(N):
    row = list(map(int, input("").split()))
    cube.append(row)

NC = int(input(""))

commands = []
for _ in range(NC):
    command = list(map(int, input("").split()))
    commands.append(command)

def rotate_cube(cube, y_offset, x_offset, width, angle):
    top = []
    left = []
    right = []
    bottom = []

    for i in range(y_offset, y_offset + width):
        for j in range(x_offset, x_offset + width):
            if i == y_offset:
                top.append(cube[i][j])
            if i == y_offset + width - 1:
                bottom.append(cube[i][j])
            if j == x_offset:
                left.append(cube[i][j])
            if j == x_offset + width - 1:
                right.append(cube[i][j])

    if angle == 1: # 90
        for i in range(y_offset, y_offset + width):
            for j in range(x_offset, x_offset + width):
                if i == y_offset:
                    cube[i][j] = right.pop(0)
                if i == y_offset + width - 1:
                    cube[i][j] = left.pop(0)
                if j == x_offset:
                    cube[i][j] = top.pop()
                if j == x_offset + width - 1:
                    cube[i][j] = bottom.pop()
    elif angle == 2: # 180
        for i in range(y_offset, y_offset + width):
            for j in range(x_offset, x_offset + width):
                if i == y_offset:
                    cube[i][j] = bottom.pop()
                if i == y_offset + width - 1:
                    cube[i][j] = top.pop()
                if j == x_offset:
                    cube[i][j] = right.pop()
                if j == x_offset + width - 1:
                    cube[i][j] = left.pop()
    elif angle == 3: # 270
        for i in range(y_offset, y_offset + width):
            for j in range(x_offset, x_offset + width):
                if i == y_offset:
                    cube[i][j] = left.pop()
                if i == y_offset + width - 1:
                    cube[i][j] = right.pop()
                if j == x_offset:
                    cube[i][j] = bottom.pop(0)
                if j == x_offset + width - 1:
                    cube[i][j] = top.pop(0)
    if width > 3:
        rotate_cube(cube, y_offset + 1, x_offset + 1, width - 2, angle)

for command in commands:
    y_offset, x_offset, width, angle = command
    rotate_cube(cube, y_offset, x_offset, width, angle)

for row in cube:
    print(" ".join(map(str, row)))
