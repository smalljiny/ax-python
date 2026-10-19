'''
설명

주어진 크기의 X를 그리는 프로그램을 작성하라.

입력

첫번째 줄에 크기 n이 주어진다. (3 <= n <= 10)

출력

n크기의 X를 출력하라.
'''
n = int(input())

for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("X", end='')
        else:
            print(" ", end='')
    print()