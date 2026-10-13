str = input()
a, b = map(int, str.split())
def sum(a, b):
    if a >= -1000 and a <= 1000 and b >= -1000 and b <= 1000:
        return a + b
    return None

print(sum(a, b))