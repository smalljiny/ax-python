'''
설명

9 X 9 크기의 격자판에 81개의 자연수 또는 0이 적혀 있습니다. 이 숫자들 중에서 가장 큰 값(최댓값)을 찾고, 그 최댓값이 몇 행 몇 열에 위치해 있는지 구하는 프로그램을 작성하세요.행 번호와 열 번호는 맨 위, 맨 왼쪽부터 1행 1열로 시작합니다.


입력

첫째 줄부터 아홉 번째 줄까지, 한 줄에 9개씩 수가 공백을 사이에 두고 주어집니다.

주어지는 수는 100 미만의 자연수 또는 0입니다.

출력

첫째 줄에 최댓값을 출력합니다.

둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 공백으로 구분하여 차례로 출력합니다.

최댓값이 두 개 이상인 경우, 그 중 아무 곳이나 한 곳의 위치만 출력해도 됩니다.
'''
n = 9

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

max_value = 0
pos_x = 1
pos_y = 1

for i in range(n): # y
    for j in range(n): # x
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            pos_x = j + 1
            pos_y = i + 1

print(f"{max_value}\n{pos_y} {pos_x}")