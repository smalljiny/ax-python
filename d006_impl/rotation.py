N = int(input(""))

table = [[0 for _ in range(N)] for _ in range(N)]

def set_round(target, size, seed, offset):
    for i in range(size):
        if i == 0:
            base = seed
            for j in range(size):
                target[i + offset][j + offset] = base
                base += 1
        if i > 0 and i < size - 1:
            target[i + offset][size - 1 + offset] = seed + size + i - 1
            target[i + offset][0 + offset] = seed + size * 3 + size - 4 - i

        else:
            base = seed + size + size + size - 3
            for j in range(size):
                target[size - 1 + offset][j + offset] = base - j

seed = 1
for i in range(N):
    size = N - i * 2
    offset = i
    set_round(table, size, seed, offset)
    seed += size * 2 + (size - 2) * 2

for row in table:
    for num in row:
        print(f"{num}", end=' ')
    print()

