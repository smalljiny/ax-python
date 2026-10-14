num = int(input())

idx = 1
current_num = num
total = 0

for idx in range(1, 6):
    total += current_num % 100
    current_num //= 100
    if current_num == 0:
        break

print(total)