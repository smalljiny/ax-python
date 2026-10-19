'''
설명

N개의 숫자로 구성된 수열과 M개의 숫자로 구성된 수열이 있다.

아래는 N=3, M=5인 두 수열의 예시이다.
image.png

두 수열의 위치를 자유롭게 움직여, 각 숫자들이 마주보는 숫자들의 위치를 변경할 수 있다.
image.png
image.png

단, 각 수열의 양 끝 범위를 벗어나게 배치할 수 는 없다.

두 수열을 적절하게 배치하여, 서로 마주보는 숫자들을 모두 곱한 뒤 더했을 때의 최대값을 구하는 프로그램을 작성하라.
위 수열의 정답은 30이 된다.
image.png

입력

첫번쨰 줄에 정수 N과 M이 공백으로 구분되어 주어진다. (3 <= N, M <= 20)
두번째 줄에는 첫번째 수열의 N개의 숫자들이 공백으로 구분되어 주어진다.
세번째 줄에는 두번째 수열의 M개의 숫자들이 공백으로 구분되어 주어진다.

출력

서로 마주 보는 숫자들을 모두 곱한 뒤 더했을 때의 최대값을 출력하라.
'''
N, M = map(int, input().split())

arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

if N > M:
    base_arr = arr_n
    compare_arr = arr_m
else:
    base_arr = arr_m
    compare_arr = arr_n

max_sum = 0;

diff_len = len(base_arr) - len(compare_arr)

for repeat in range(diff_len + 1):
    current_sum = 0
    for idx in range(len(compare_arr)):
        current_sum += base_arr[idx + repeat] * compare_arr[idx]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
