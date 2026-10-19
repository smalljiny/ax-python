'''
설명

두 정수를 더하는 수식이 주어지면, 이 수식의 결과를 출력하는 프로그램을 작성하시오.

입력

첫번째 줄에 두 정수를 더하는 수식이 주어진다.

각 값은 0 이상, 100 이하의 정수이다.
출력

수식의 결과를 출력한다.
'''
str = input()

split_str = str.split('+')

left_num = int(split_str[0])
right_num = int(split_str[1])

print(left_num + right_num)