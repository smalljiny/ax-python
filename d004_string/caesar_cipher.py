codes = input()
key = int(input())

encrypted = ""

print(ord('z'))

for code in codes:
    if code == ' ':
        encrypted += ' '
        continue
    
    tmp = ord(code) + key

    if tmp > ord('z'):
        tmp -= 26
    encrypted += chr(tmp)

print(encrypted)