'''
설명

2개의 단어가 주어졌을 때, 공통적으로 가진 문자를 알파벳순으로 출력하는 프로그램을 작성하시오.

입력

첫번째 줄에 단어 a, b가 공백으로 구분되어 주어진다. (1 <= a, b의 길이 <= 10)
두 단어는 모두 영문 소문자로 주어진다.

출력

a와 b에 공통적으로 사용된 문자를 알파벳 순으로 공백 없이 출력한다.
'''
words = list(map(str, input().split()))

set_1st_word = set(words[0])
set_2nd_word = set(words[1])

common_chars = sorted(set_1st_word & set_2nd_word)

print(''.join(common_chars))