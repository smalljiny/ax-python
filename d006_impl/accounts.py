def split_letter(id):
    tmp = '';
    for idx in range(len(id)):
        if id[idx].isalpha():
            tmp += id[idx]
        else:
            break
    return tmp

def split_digit(id, str_part):
    num = id[len(str_part):]
    return int(num) if num.isdigit() else 0

registered_id = {
    # id: []
}

N = int(input())
ids = list(map(str, input().split()))
new_id = input()

for id in ids:
    str_part = split_letter(id)
    num_part = split_digit(id, str_part)
    if str_part not in registered_id:
        registered_id[str_part] = [num_part]
    else:
        registered_id[str_part].append(num_part)

for item in registered_id:
    registered_id[item].sort()

str_part = split_letter(new_id)
num_part = split_digit(new_id, str_part)

if str_part not in registered_id:
    print(new_id)
else:
    num_parts = registered_id[str_part]
    if num_part in num_parts:
        for idx in range(1, len(num_parts) + 1):
            if idx == len(num_parts):
                print(f"{str_part}{num_parts[idx-1] + 1}")
                break
            elif num_parts[idx] != num_parts[idx-1] + 1:
                print(f"{str_part}{num_parts[idx-1] + 1}")
                break
    else:
        print(new_id)
