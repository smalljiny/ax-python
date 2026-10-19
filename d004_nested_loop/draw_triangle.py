'''
설명

정수 n을 입력 받아 첫째줄에는 별 1개, 둘째줄에는 별 2개... n번째 줄에 별 n개를 출력하는 프로그램을 작성하시오.
별은 우측 정렬된 상태로 출력 되어야 한다.

입력

첫번째 줄에 정수 n이 주어진다. (1 <= n <= 10)

출력

규칙대로 별을 출력한다.
'''
num = int(input())

for i in range(num):
    for j in range(num):
        if (j > num - i - 2):
            print("*", end='')
        else:
            print(" ", end='')
    print()