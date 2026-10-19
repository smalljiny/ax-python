'''
설명

n개의 숫자들이 주어졌을 때, 숫자들을 한 칸 씩 앞으로 땡겨 주세요.
맨 앞에 있던 숫자는 맨 뒤로 가게 됩니다.

입력

첫번쨰 줄에 숫자의 개수 n이 주어집니다. (1 <= n <= 10)
두번째 줄에 n개의 숫자가 공백으로 구분되어 주어집니다.

출력

숫자들을 한 칸씩 땡긴 후의 숫자들을 출력합니다.
'''
n = int(input())
data = list(map(int, input().split()))

tmp = data[0]

for idx in range(len(data) - 1):
    data[idx] = data[idx + 1]
data[len(data) - 1] = tmp

print(' '.join(map(str, data)))