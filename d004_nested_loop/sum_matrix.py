'''
설명

행렬은 숫자들을 격자 형태로 나열한 구조로, 두 행렬의 크기가 같을 때 같은 위치(행과 열)에 있는 원소끼리 더하는 '행렬의 덧셈' 연산을 수행할 수 있습니다.
N X M 크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더한 결과 행렬을 구하는 프로그램을 작성하시오.

입력

첫째 줄에 행렬의 크기 N 과 M 이 공백을 사이에 두고 주어집니다. (
1
≤
N
,
M
≤
100
1≤N,M≤100)
둘째 줄부터N개의 줄에 걸쳐 행렬A의 원소 M개가 차례대로 주어집니다.
이어서 다음 N개의 줄에 걸쳐 행렬 B의 원소M개가 차례대로 주어집니다.
행렬의 각 원소는 절댓값이 100 이하인 정수입니다.
출력

첫째 줄부터 N개의 줄에 걸쳐 행렬 A와 B를 더한 결과를 출력합니다.
각 줄의 원소는 공백으로 구분하여 출력합니다.
'''
N, M = map(int, input().split())

matrix_0 = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix_0.append(row)

matrix_1 = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix_1.append(row)

result = [] 
for i in range(N):
    row_result = []
    for j in range(M):
        row_result.append(matrix_0[i][j] + matrix_1[i][j])        
    result.append(row_result)

for row in result:
    print(' '.join(map(str, row)))