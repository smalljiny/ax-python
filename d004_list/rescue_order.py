'''
설명

우주선 비상 탈출 시 탑승 명단이 입력되었습니다.
구조선이 도착하면 맨 나중에 탑승한 사람부터 순서대로 구조 작업을 진행해야 합니다.
전체 인원수 N과 탑승자 명단을 입력받아 가장 나중에 탑승한 사람부터 거꾸로 출력하는 프로그램을 작성하시오.

입력

첫째 줄에 인원수 N 이 주어집니다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에 걸쳐 탑승자 이름이 한 줄에 하나씩 주어집니다.

출력

마지막 탑승자부터 첫 번째 탑승자까지 거꾸로 한 줄에 하나씩 출력해주세요.
'''
n = int(input())
passengers = []

for idx in range(n):
    passengers.append(input())

for passenger in passengers[::-1]:
    print(passenger)