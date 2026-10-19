'''
설명

지우는 주말에 가족들과 등산을 가기로 했다.
알고리즘 공부에 매진하는 지우는 평소 운동을 하지 않았기 때문에 체력이 좋지 않아 오르막길을 극도로 싫어한다.

미리 마음의 준비를 하기 위하여 인터넷을 통해 주말에 가게 될 산을 조사하여 등산로의 구간별 높이 H를 확인하고,
N개의 구간 중 오르막이 가장 심한 구간이 어디인지 찾으려고 한다.

● 오르막길은 i번 구간보다 i+1번 구간의 높이가 더 높은 것을 의미한다.
● 구간 사이의 차이 값(H_i)이 클수록 오르막이 심하다는 것을 의미한다.

입력

첫 번째 줄에 구간의 수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄부터 N + 1 번째 줄에 걸쳐 i번에서 i+1번의 구간의 높이 H_i(0 ≤ H_i ≤ 1,000,000,000)가 주어진다.

출력

첫 번째 줄에 오르막이 가장 심한 구간의 순번을 공백으로 구분하여 출력한다.

오르막이 가장 심한 구간이 2개 이상이라면, 먼저 만나는 구간을 출력한다.

만약 오르막이 없다면, 0을 출력한다.
'''
n = int(input())
max_diff = 0
last_height = 0
has_climb = False
range_max_diff = [0, 0]

for i in range(n):
    if i == 0:
        last_height = int(input())
        continue
    height = int(input())
    diff = height - last_height
    if diff > max_diff:
        has_climb = True
        range_max_diff = [i, i + 1]
        max_diff = diff
    last_height = height

if has_climb:
    print(' '.join(map(str, range_max_diff)))
else:
    print(0)