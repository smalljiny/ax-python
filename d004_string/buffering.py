'''
설명

인터넷이 너무 느려 내가 전송한 메세지의 문자가 다음과 같이 전송되고 있다.

hello
->
h
he
hel
hell
hello
내가 전송한 메세지가 어떻게 전송될지를 출력하는 프로그램을 작성하라.

입력

첫번째 줄에 메세지의 내용을 담은 문자열 S가 주어진다. (1 <= S의 길이 <= 20)
메세지에 공백은 존재하지 않는다.

출력

버퍼링되어 출력되는 각 문자열을 한 줄에 공백없이 출력한다.
'''
str = input()

buffered = ""
word = ""

for char in str:
    word += char
    buffered += word

print(buffered)