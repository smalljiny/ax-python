'''
설명

두 개의 점의 위치가 주어졌을 때, 두 점의 맨하탄 거리를 구하는 프로그램을 작성하세요.
맨하탄 거리는 두 점의 가로, 세로의 길이의 합을 의미합니다.
image.png

입력

첫번째 줄에 점 A의 위치 (y1, x1)가 주어집니다. (0 <= y1, x1 <= 100)
두번째 줄에 점 B의 위치 (y2, x2)가 주어집니다. (0 <= y2, x2 <= 100)

출력

두 점의 맨하탄 거리를 구하여 출력합니다.
'''

y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())

if y1 > y2:
    dy = y1 - y2
else:
    dy = y2 - y1

if x1 > x2:
    dx = x1 - x2
else:
    dx = x2 - x1

manhattan = dy + dx

print(manhattan)