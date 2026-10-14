'''
설명

두 수가 주어졌을때, 첫 번째 숫자가 두 번째 숫자의 약수이면 factor, 첫 번째 숫자가 두 번째 숫자의 배수이면 multiple, 둘 다 아니면 neither을 출력하시오.

입력

두 개의 정수가 주어진다. 두 정수는 서로 같지않음을 보장한다.

출력

문제 설명에 맞게 출력하시오.
'''

N1, N2 = map(int, input().split())

if N2 % N1 == 0:
    print("factor")
elif N1 % N2 == 0:
    print("multiple")
else:
    print("neither")