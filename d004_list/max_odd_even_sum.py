'''
설명

7개의 자연수 중, 가장 큰 홀수와 가장 큰 짝수의 합을 구하는 프로그램을 작성하시오.

입력

첫번째 줄에 7개의 자연수가 공백으로 구분되어 주어진다.
모든 숫자는 100보다 작은 수이다.

출력

가장 큰 홀수와 가장 큰 짝수의 합을 출력한다.
홀수 또는 짝수가 존재하지 않으면, 0으로 취급한다.
'''
data = list(map(int, input().split()))

max_odd = 0
max_even = 0

for num in data:
    if num % 2 == 0 and num > max_even:
        max_even = num
    elif num % 2 != 0 and num > max_odd:
        max_odd = num

print(max_odd + max_even)