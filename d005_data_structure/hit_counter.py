'''
설명

N개의 숫자가 주어졌을 때, 각 숫자가 몇 번 등장했는지 출력하는 프로그램을 작성하라.

입력

첫 번째 줄에 수열의 크기 N, 질의의 수 M이 입력됩니다. ( 1 <= M <= N <= 100,000)
두 번째 줄에 N 개의 정수가 공백으로 구분되어 입력됩니다.
주어지는 정수는 1부터 10억 사이의 정수임이 보장됩니다.
세 번째 줄에는 M개의 정수가 공백으로 구분되어 입력됩니다.

출력

첫 번째 줄에 M개의 정수들에 대해 각각 몇개씩 존재하는지를 공백으로 구분해서 출력합니다.
'''
N, M = map(int, input().split())

data = list(map(int, input().split()))
targets = list(map(int, input().split()))

counter = {}

for num in data:
    if num not in counter:
        counter[num] = 0
    counter[num] += 1

for target in targets:
    print(counter.get(target, 0), end=' ')