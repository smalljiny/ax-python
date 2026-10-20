'''
설명

로마 숫자는 I, V, X, L, C, D, 그리고 M으로 표기한다.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
예를 들어, 2는 II로 쓰고, 12는 XII로 쓴다.

로마 숫자는 일반적으로 큰 심볼부터 쓰기 시작한다.
하지만 4는 IIII가 아닌, IV이다. 5(V) 전에 1(I) 이 있는 것 처럼 작은 수가 먼저 오면, 뺀다는 의미이다.
그렇기에 9 역시 IX와 같이 쓴다.

빼기가 사용되는 경우는 다음과 같이 6 경우가 있다.

I는 V와 X전에 사용되어 4 또는 9를 표현한다.
X는 L과 C 전에 사용되어 40과 90을 표현한다.
C는 D와 M 전에 사용되어 400과 900을 표현한다.
로마 숫자가 주어졌을 때, 정수로 변환하는 프로그램을 작성하라.

입력

첫번째 줄에 로마 숫자로 표현된 문자열 S가 주어진다. (1 <= S의 길이 <= 15)
S는 I, V, X, L, C, D, M의 문자로만 이루어져 있다.
S는 1부터 3999 범위 내의 정수로 표현 가능함이 보장된다.

출력

주어진 로마 숫자를 정수로 변환한 값을 출력한다.
'''
roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

roman_string = input()

number = 0
idx = 1
while idx < len(roman_string):
    char = roman_string[idx - 1]
    next_char = roman_string[idx]

    if (char == 'I' and next_char == 'V') \
        or (char == 'I' and next_char == 'X') \
        or (char == 'X' and next_char == 'L') \
        or (char == 'X' and next_char == 'C') \
        or (char == 'C' and next_char == 'D') \
        or (char == 'C' and next_char == 'M'):
        number += roman_numerals[next_char] - roman_numerals[char]
        idx += 2
        continue
    else:
        number += roman_numerals[char]
        idx += 1
    if idx == len(roman_string):
        number += roman_numerals[next_char]
print(number)