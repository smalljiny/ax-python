'''
설명

n개의 수열이 주어졌을 때, 첫번째 숫자와 마지막 숫자가 같다면 true, 아니면 false를 출력하는 프로그램을 작성하세요.
만약 수열에 숫자가 단 하나밖에 없어도 true를 출력합니다.

입력

첫번쨰 줄에 수열에 포함된 숫자의 수 n이 주어집니다. (1 <= n <= 100)
두번째 줄에 n개의 숫자들이 공백으로 구분되어 주어집니다. (1 <= 숫자 <= 100)

출력

만약 첫번째와 마지막 숫자가 같거나, 수열에 숫자가 1개밖에 없다면 true를 출력합니다.
그렇지 않다면 false를 출력합니다
'''
n = int(input())
data = list(map(int, input().split()))

if len(data) == 1 or data[0] == data[len(data) - 1]:
    print('true')
else:
    print('false')