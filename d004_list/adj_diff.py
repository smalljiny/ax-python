'''
설명

길이가 n인 정수 배열 arr을 입력받습니다.
배열에서 인접한 두 수에 대해, 앞의 수를 뒤의 수에서 뺀 값의 절댓값을 구하여 순서대로 출력하세요.

입력

자연수 n과 배열 arr을 입력하시오.

출력

인접한 두 숫자 ( 왼쪽숫자 - 오른쪽숫자) 를 차례대로 출력하시오.
'''
n = int(input())
data = list(map(int, input().split()))

for idx in range(len(data) - 1):
    print(abs(data[idx] - data[idx + 1]), end=' ')