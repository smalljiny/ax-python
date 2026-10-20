N = int(input())
encoded_message = input()

code_map = {
'000000': 'A',
    '001111': 'B',
    '010011': 'C',
    '011100': 'D',
    '100110': 'E',
    '101001': 'F',
    '110101': 'G',
    '111010': 'H'
}

code_keys = list(code_map.keys())
decoded = ''
error_index = -1

for i in range(N):
    chunk = encoded_message[i*6:(i+1)*6]
    if chunk in code_map:
        decoded += code_map[chunk]
    else:
        has_replacement = False
        for key in code_keys:
            diff_count = 0
            for chunk_idx in range(len(chunk)):
                if chunk[chunk_idx] != key[chunk_idx]:
                    diff_count += 1
            if diff_count == 1:
                decoded += code_map[key]
                has_replacement = True
                break
        if not has_replacement:
            error_index = i + 1
            break

if error_index != -1:
    print(error_index)
else:
    print(decoded)