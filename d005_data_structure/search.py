N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

n = int(input())

targets = list(map(int, input().split()))
filtered_targets = set(targets)
results = {}

for x in range(N):
    for y in range(M):
        if matrix[x][y] in filtered_targets:
            if matrix[x][y] not in results:
                results[matrix[x][y]] = []
            results[matrix[x][y]].append((x, y))

for target in targets:
    if target not in results:
        print("none", end=" ")
    else:
        for position in results[target]:
            print(f"({position[0]},{position[1]})", end=" ")
    
    print()