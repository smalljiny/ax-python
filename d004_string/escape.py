codes = input()

total = 0
secret = ""
count = 0
for code in codes:
    if code in "0123456789":
        if count < 4:
            secret += code
            count += 1
        else:
            total += int(secret)
            secret = ""
            secret += code
            count = 1
    else:
        if secret:
            total += int(secret)
        secret = ""
        count = 0

print(str(total)[:4])