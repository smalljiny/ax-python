'''
설명

3 x 3 크기의 블록을 활용하여 픽셀 그림을 그리려고 한다.

N×N 크기의 정사각형 도화지가 0으로 색칠되어 있다.
도화지의 가장 왼쪽 위의 칸은 (1,1)칸이고, 가장 오른쪽 아래 칸은 (N,N)칸이다.

도화지에 총 M번을 색칠한다.
좌표 (y,x)가 주어지면, (y,x)를 왼쪽 위 꼭지점으로 하여 3 x 3 크기의 블록 픽셀로 색칠한다.
색칠한 칸은 1로 표현한다.

도화지의 크기 N과 색칠의 횟수 M이 주어졌을 때, 완성된 그림을 출력하는 프로그램을 작성하라.

입력

첫번째 줄에 두 정수 N과 M이 주어진다. (3 ≤ N, M ≤ 50)
두번째 줄부터 M줄에 걸쳐 두 정수 y와 x가 주어진다. (1 ≤ y, x ≤ N−2)

출력

색칠이 완료된 N × N 크기의 도화지를 출력한다.
'''
N, M = map(int, input().split())

paintings = []

for i in range(M):
    x, y = map(int, input().split())
    paintings.append([x -1, y - 1])

for i in range(N):
    for j in range(N):
        is_inside = False
        for px, py in paintings:
            if (px <= i and px + 3 > i) and (py <= j and py + 3 > j):
                is_inside = True

        if is_inside:
            print("1", end=' ')
        else:
            print("0", end=' ')
    print()
