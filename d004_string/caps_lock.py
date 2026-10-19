'''
설명

N길이의 단어 하나를 타이핑하다가 어느 순간부터 CAPS LOCK을 눌러 대문자로 출력 되었다.
CAPS LOCK을 누른 시점 K가 주어졌을 때, 원래 치고자 했던 단어를 출력하라.

입력

첫번째 줄에 단어의 길이 N과 CAPS LOCK을 누른 시점 K가 주어진다. (1 <= K <= N <= 100)
두번째 줄에 N길이의 단어가 주어진다.

단어에 공백은 존재하지 않는다.
단어는 영문으로만 주어짐이 보장된다.
K번째 이후의 문자들은 모두 대문자임이 보장된다.
출력

원래 치려 했던 단어를 출력한다.
'''
length, pos_caps = map(int, input().split())
str = input()

str = str[:pos_caps - 1] + str[pos_caps - 1:].lower()
print(str)