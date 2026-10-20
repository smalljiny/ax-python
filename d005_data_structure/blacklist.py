'''
설명

용순이는 드디어 원룸에서 벗어나 아파트로 이사를 가려 합니다.
하지만 폭등한 부동산 사태로 인해, 비교적 저렴한 아파트를 찾아 들어갈 수 밖에 없었습니다.
하지만 H x W 크기의 더 넓은 아파트로 이사한 것에 대해 너무 행복했습니다.

image.png

하지만 입주를 하고 나서 보니, 이 아파트 내에는 악명 높은 블랙리스트들이 존재하는 것을 알았습니다.
민철이는 블랙리스트의 목록이 적힌 BH x BW 크기의 종이를 주민 회의에서 입수했습니다.

블랙리스트에 등록된 시민이 살고있는 아파트 호실의 총 개수와
블랙리스트에 해당되지 않는 선량한 시민이 있는 아파트 호실의 총 개수를 구해주세요.

입력

첫번째 줄에 아파트의 크기 H와 W가 공백으로 구분되어 입력됩니다. (1 ≤ H, W ≤ 1,000)
그리고 두번째 줄부터 H개의 줄에 걸쳐 W개의 주민 번호가 공백으로 구분되어 입력됩니다. (0 ≤ 주민 번호 ≤100,000)
아파트에 거주하는 시민들의 주민 번호는 중복된 값이 존재할 수 있습니다.

다음 줄에는 블랙리스트의 정보를 나타내는 종이의 세로 크기 BH와 가로 크기 BW가 공백으로 구분되어 입력됩니다. (1 ≤ BH, BW ≤ 1,000)
그리고 다음 줄부터 BH개의 줄에 걸쳐 BW개의 주민 번호가 공백으로 구분되어 입력됩니다. (0 ≤ 주민 번호 ≤100,000)
블랙리스트 종이에 적힌 주민 번호는 중복된 값이 존재할 수 있습니다.

출력

첫 번째 줄에 블랙리스트에 등록된 시민이 살고 있는 아파트 호실이 총 몇 개인지 출력합니다.
두 번째 줄에 블랙리스트에 등록되지 않은 선량한 시민의 호실이 총 몇 개인지 출력합니다.
'''
H, W = map(int, input().split())

resident = {}
for _ in range(H):
    row = list(map(int, input().split()))
    for id in row:
        if resident.get(id) is None:
            resident[id] = 1
        else:
            resident[id] += 1

BH, BW = map(int, input().split())

blacklist = set()
for _ in range(BH):
    row = list(map(int, input().split()))
    blacklist.update(row)

blacklist_count = 0;
whitelist_count = 0;

for id, room_count in resident.items():
    if id not in blacklist:
        whitelist_count += room_count
    else:
        blacklist_count += room_count

print(blacklist_count)
print(whitelist_count)