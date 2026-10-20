alphabets = input()

filtered_alphabets = set()

for alphabet in alphabets:
    filtered_alphabets.add(alphabet)

print(''.join(sorted(filtered_alphabets)))