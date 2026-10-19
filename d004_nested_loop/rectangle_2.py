'''
정사각형의 한 변의 길이 n을 입력받은 후 다음과 같은 정사각형 형태로 출력하는 프로그램을 작성하시오.

1 2 3 4 5 
5 4 3 2 1 
1 2 3 4 5 
5 4 3 2 1 
1 2 3 4 5

입력

첫번째 줄에 정사각형의 한 변의 길이 n이 주어진다. (1 <= n <= 100)

출력

형식에 맞춰 숫자 사각형을 출력한다.
각 숫자 사이는 공백으로 구분하여 출력한다.
'''
num = int(input())

for i in range(1, num + 1):
    if i % 2 != 0:
        for j in range(1, num + 1):
            print(j, end=' ')
    else:
        for j in range(num, 0, -1):
            print(j, end=' ')
    print()