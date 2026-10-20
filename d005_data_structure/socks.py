'''
설명

지우는 동대문에서 양말 장사를 하고 있다.
모든 양말은 쌍(2개)으로 판매해야 하는데, 바람에 하나가 날아가 버렸다.
그렇기에 한 짝만 남은 양말은 팔 수 없게 되었다.
2N-1개의 남은 양말들의 대한 정보가 주어졌을 때, 판매하지 못하는 양말의 번호를 찾는 프로그램을 작성하시오.

입력

첫번째 줄에 양말 쌍의 수 N이 주어진다. (1 <= N <= 100)
두번째 줄에 2N-1개의 양말의 번호가 공백으로 구분되어 주어진다.
동일한 숫자는 최대 2개가 존재함이 보장된다.

출력

1짝만 남아 판매할 수 없는 양말 번호를 출력한다.
'''
n = int(input())

socks = list(map(int, input().split()))

counter = {}

for sock in socks:
    if sock not in counter:
        counter[sock] = 0
    counter[sock] += 1

for sock, count in counter.items():
    if count == 1:
        print(sock)
        break