'''
설명

"내 보물말인가? 가지고싶다면 주지." 
"찾아라 이 세상을 모든 곳에 두고 왔다!"
해적왕 실버 로버가 처형을 당하면서 한 말 한마디에 대해적시대가 열렸다.

새로운 해적왕을 꿈꾸는 루디는 수년간의 모험과 난관을 해쳐나가며 드디어 해적왕의 보물이 숨겨진 위치를 해석할 수 있는 비밀지도를 입수하였다.

이 비밀 지도는 암호화된 채로 2개로 나눠져 있으며, 두 지도를 합쳐 해독해야 한다.

비밀 지도를 해독하는 과정은 다음과 같다.

2개의 지도는 각각 N길이의 정수로 암호화되어있다. 이 정수들을 2진수로 풀어 각각의 지도를 복원해야 한다.
입수한 두개의 지도가 [9, 20, 28, 18, 11] 그리고 [30, 1, 21, 17, 28] 이라면, 이 둘을 복원한 지도는 다음과 같다.
image.png
image.png

해독된 2개의 지도를 합친다.
양쪽 다 0으로 기록된 기간은 놔두고, 한쪽이라도 1로 된 공간은 1로 표기한다.
즉, 완벽히 복원된 비밀지도의 결과는 다음과 같다.
image.png

2개의 비밀 지도의 정보가 주어졌을 때, 완벽히 복원된 지도를 출력하는 프로그램을 작성하라.

입력

첫번째 줄에 지도의 한 변 크기 N이 주어진다. (1 <= N <= 16)
완벽히 복원된 지도의 크기는 N x N이다.
두번째 줄에는 지도 A의 정보를 나타내는 N개의 정수가 공백으로 구분되어 주어진다.
세번째 줄에는 지도 B의 정보를 나타내는 N개의 정수가 공백으로 구분되어 주어진다.
정수 배열의 각 원소를 2진수로 변환했을 때의 길이는 N 이하임이 보장된다.

출력

완벽히 복원된 비밀 지도를 출력한다.
1인 곳은 "#", 0인 곳은 "_"로 출력한다.
'''
n = int(input())
map_1 = map(int, input().split())
map_2 = map(int, input().split())

def conv_to_binary_map(encryted_map):
    treasure_map = []
    for number in encryted_map:
        map_row = []
        quotient = number // 2
        remainder = number % 2
        map_row.append(remainder)

        while quotient > 0:
            number = quotient
            quotient = number // 2
            remainder = number % 2
            map_row.append(remainder)

        if len(map_row) < n:
            map_row.extend([0] * (n - len(map_row)))

        map_row.reverse()
        treasure_map.append(map_row)

    return treasure_map

decrypted_map_1 = conv_to_binary_map(map_1)
decrypted_map_2 = conv_to_binary_map(map_2)

for x in range(n):
    for y in range(n):
        if decrypted_map_1[x][y] == 1 or decrypted_map_2[x][y] == 1:
            print("#", end="")
        else:
            print("_", end="")
    print()