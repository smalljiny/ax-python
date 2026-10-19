'''
설명

n개의 정수가 주어졌을 때, 정수 중 짝수의 개수를 세는 프로그램을 작성하라.

입력

첫번째 줄에 정수의 개수 n이 주어진다. (1 <= n <= 100)
두번째 줄에 n개의 정수가 공백으로 구분되어 주어진다. (0 <= 각 정수 <= 20)

출력

n개의 정수 중 짝수의 개수를 출력한다.
'''
n = int(input())
data = list(map(int, input().split()))

count = 0

for idx in range(len(data)):
    if data[idx] % 2 == 0:
        count += 1

print(count)