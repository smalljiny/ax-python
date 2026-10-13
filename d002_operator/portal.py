'''
설명

이슬이는 1직선의 길에서 a 좌표에 있다.
그의 목표는 b의 좌표로 이동하는 것이다.

2085년인 지금은 더 이상 이동수단이 없고, 순간이동을 해주는 포탈들이 배치되어 있다.
현재 길에서는 x좌표에서 y 좌표로, 또는 y좌표에서 x좌표로 이동하는 한 개의 포탈이 설치되어 있다.
물론, 무조건 포탈을 이용해야 하는 것은 아니다.

이슬이의 출발지와 목적지인 a, b, 그리고 포탈을 잇는 좌표 x, y가 주어졌을 때, a에서 b로 가는 최소 거리를 구하여라.

한 칸을 1의 거리로 책정한다.
포탈을 활용할 때는 이동 거리로 고려하지 않는다.
입력

네 정수 a,b,x,y가 공백을 사이에 두고 주어진다. (1 <= a, b, x, y <= 100)

출력

a에서 b로 가는 최소 거리를 출력한다.
'''

a, b, x, y = map(int, input().split())

direct_distance = abs(a - b)

distance_ax = abs(a - x)
distance_ay = abs(a - y)

distance_bx = abs(b - x)
distance_by = abs(b - y)

distance_a = min(distance_ax, distance_ay)
distance_b = min(distance_bx, distance_by)

minimum_distance = min(direct_distance, distance_a + distance_b)

print(minimum_distance)