'''
설명

2개의 주사위를 던져 눈금의 합이 N이 나올 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

입력

첫번째 줄에 목표 눈금의 합 N이 주어진다.
만약 해당 눈금을 만들 수 없다면 0을 출력한다.

출력

N을 굴릴 수 있는 눈금의 경우의 수를 출력한다.
'''
target = int(input())

count = 0

for d1 in range(1, 7):
    for d2 in range(1, 7):
        if (d1 + d2 == target):
            count += 1
print(count)