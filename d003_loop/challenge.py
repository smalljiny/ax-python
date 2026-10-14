threshold = int(input())

idx = 1
value = 1

while True:
    value *= idx

    if value >= threshold:
        print(value)
        break
    idx += 1