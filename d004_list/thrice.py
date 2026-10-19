'''
설명

n개의 숫자들이 주어졌을 때, 연속으로 홀수 또는 짝수가 3번 이상 발생하는 수열이 존재하는지 구하는 프로그램을 작성하시오.

입력

첫번째 줄에 숫자의 개수 n이 주어진다. (1 <= n <= 10)
두번째 줄에 n개의 숫자가 공백으로 구분되어 주어진다. (1 <= 숫자 <= 10)

출력

만약 3연속으로 홀수 또는 짝수가 발생한다면 true, 아니면 false를 출력한다.
'''
n = int(input())
data = list(map(int, input().split()))

result = 'false'

for idx in range(len(data) - 2):
    if data[idx] % 2 == 0 and data[idx + 1] % 2 == 0 and data[idx + 2] % 2 == 0:
        result = 'true'
        break
    elif data[idx] % 2 != 0 and data[idx + 1] % 2 != 0 and data[idx + 2] % 2 != 0:
        result = 'true'
        break

print(result)
