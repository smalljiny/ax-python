'''
설명

N X N크기의 격자 무늬 중 두 좌표를 클릭하면 선택한 컬러로 생성되는 사각형 영역이 이 칠해지는 Paint Tool 이 있습니다.
아래는 3번 컬러로 (1,1) 과 (4,4)를 클릭했을 때의 예시입니다.
50b8c1944b.png

컬러 값이 클 수록 더 진한 색을 의미합니다.
그리고 더 진한 색은 더 옅은 색 위에 색이 덮어씌워집니다.
아래는 7번 컬러로 (2,3)과 (7,3)을 클릭했을 때의 예시입니다.
5173a7cb14.png

특정 칸들의 3들이 7로 덮어 씌워진 것을 확인할 수 있습니다.
아래는는 (3, 2)와 (8,6)을 6번 컬러로 클릭했을 때의 예시입니다.
e19389fe66.png
6번 컬러는 7번 컬러보다 옅은 색이기에, 7이 덮어 씌워지지 않습니다.

이 Paint Tool로 완성된 그림이 주어졌을 때, 한 컬러로 이루어진 가장 큰 정사각형의 면적를 찾는 프로그램을 작성해 주세요.
아래는 위에서 만들어진 그림에서 가장 큰 정사각형의 면적인 9를 나타내는 예시 중 하나입니다.
6cb3720964.png

입력

첫번째 줄에는 캔버스의 한 변의 크기 N이 입력 됩니다. (1 ≤ N ≤ 10)
두번째 줄에는 색칠할 좌표의 개수 Q가 입력으로 주어집니다. (1 ≤ Q ≤ 10,000)
다음 줄 부터 Q개의 줄 만큼 5개의 숫자(color, y1, x1, y2, x2)들이 입력으로 주어집니다.
y1, x1은 사각형 영역의 한 모서리 좌표를 의미 합니다. (0 ≤ y1, x1 < 10)
y2, x2는 사각형 영역의 다른 하나의 모서리 좌표를 의미 합니다. (0 ≤ y2, x2 < 10)
단, (y1, x1)이 왼쪽 위 좌표, (y2, x2)가 오른쪽 아래 좌표임은 보장되지 않습니다.
color는 색칠할 컬러를 의미합니다. (1 ≤ color < 10)

출력

완성된 예술품에서 한 색으로 칠해져있는 가장 큰 사각형의 면적을 출력합니다.
'''
N = int(input())
Q = int(input())

def max_area(canvas):
    N = len(canvas)
    max_area = 0
    prev_color = None
    for y in range(N):
        for x in range(N):
            if canvas[y][x] == 0:
                continue
            if canvas[y][x] != prev_color:
                prev_color = canvas[y][x]
                xp = x
                yp = y
                area = 0
                while xp < N and yp < N:
                    if canvas[yp][xp] == prev_color:
                        area += 1
                    else:
                        break
                    yp += 1
                    xp += 1
                max_area = max(max_area, area)
    return max_area * max_area

canvas = [[0] * N for _ in range(N)]

for _ in range(Q):
    (color, y1, x1, y2, x2) = map(int, input().split())

    x_start = min(x1, x2)
    y_start = min(y1, y2)
    x_end = max(x1, x2)
    y_end = max(y1, y2)

    for y in range(y_start, y_end + 1):
        for x in range(x_start, x_end + 1):
            if canvas[y][x] < color:
                canvas[y][x] = color

print(max_area(canvas))