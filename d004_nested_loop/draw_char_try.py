'''
설명

삼각형의 높이 n을 입력 받고, 아래와 같이 'A'부터 순서대로 맨 오른쪽 가운데 행부터 차례대로 채워 삼각형 모양을 출력하는 프로그램을 작성하라.

오른쪽 가운데 행에 문자 'A'를 채우고, 왼쪽 열로 이동하여 위에서부터 아래로 채워나간다.
가장 왼쪽 행까지 반복하여 모두 채운다.
문자 'Z' 이후에는 다시 'A'로 돌아가 반복한다.
n=5일때의 예시

E               
F B             
G C A           
H D             
I               

입력

첫번째 줄에 삼각형의 높이 n이 주어진다. (1 <= n <= 100)
n은 홀수가 주어짐이 보장도니다.

출력

높이가 n인 문자 삼각형을 출력한다.
문자 사이에는 하나의 공백을 출력한다.
'''
n = int(input())

for i in range(n):
    for j in range(n):
        offset = 0
        for k in range(j + 1, n // 2  + 1):
            offset += n - k * 2
        offset += i - j
        offset %= 26
        offset += 65 # 대문자 알파벳
        if i <= n // 2 and j <= i:
            print(chr(offset), end=' ')
        elif i > n // 2 and j < (n - i):
            print(chr(offset), end=' ')
        else:
            print(" ", end=' ')

    print()