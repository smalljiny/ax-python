'''
설명

n개의 정수가 주어졌을 때, 해당 수열의 중앙평균값을 구하는 프로그램을 작성하시오.
중앙평균값이란, 수열의 가장 큰 값과 가장 작은 값을 제외한 나머지 값들의 평균입니다.
만약 가장 큰 값과 가장 작은 값이 2개 이상이라면, 모두 제외하는 것이 아닌, 단 하나의 값만을 제외합니다.

입력

첫번째 줄에 정수의 수 n이 주어집니다 (3 <= n <= 100)
두번째 줄에 n개의 정수가 공백으로 구분되어 주어집니다. (-100 <= 정수 <= 100)

출력

수열의 중앙평균값을 구합니다.
'''
n = int(input())
data = list(map(int, input().split()))

min = 100
max = -100
total = 0

for idx in range(len(data)):
    if data[idx] < min:
        min = data[idx]
    if data[idx] > max:
        max = data[idx]
    total += data[idx]

total -= (min + max)
median = int(total / (len(data) - 2))

print(median)