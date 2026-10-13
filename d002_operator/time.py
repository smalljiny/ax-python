'''
설명

초 단위의 정수 N을 입력 받고, N이 몇일 몇시간 몇분 몇초인지를 구하는 프로그램을 작성하세요.

입력

첫번째 줄에 초를 나타내는 정수 N이 주어진다. (1 <= N <= 1,000,000,000)

출력

다음과 같은 포맷으로 정답을 출력한다.

x일 x시간 x분 x초
'''

nsec = int(input())

day = nsec // 86400
hour = (nsec % 86400) // 3600
minute = (nsec % 3600) // 60
second = nsec % 60

print(f"{day}일 {hour}시간 {minute}분 {second}초")