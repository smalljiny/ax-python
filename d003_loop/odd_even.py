'''
설명

정수 N이 주어졌을 때, 1부터 N까지 홀수는 더하고, 짝수는 뺀 결과를 출력하는 프로그램을 작성하시오.

입력

첫번째 줄에 정수 N이 주어진다. (1 <= N <= 10)

출력

홀수는 더하고, 짝수는 뺀 결과를 출력한다.
'''
N = int(input())

result = 0;

for idx in range(1, N + 1):
    if idx % 2 == 0:
        result -= idx
    else:
        result += idx

print(result)