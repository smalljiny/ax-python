DAY_IN_MONTH = [
31,
28,
31,
30,
31,
30,
31,
31,
30,
31,
30,
31
]

def day_of_year(month, day):
    days = day
    for m in range(0, month - 1):
        days += DAY_IN_MONTH[m]
    return days

BRONZE = 0
SILVER = 1
GOLD = 2
PLATINUM = 3
DIAMOND = 4

def get_grade(recent_purchase):
    if recent_purchase < 10000:
        return BRONZE
    elif recent_purchase < 20000:
        return SILVER
    elif recent_purchase < 50000:
        return GOLD
    elif recent_purchase < 100000:
        return PLATINUM
    else:
        return DIAMOND

user_info = []

for i in range(365):
    user_info.append({
        'purchase': 0, # 해당일 구매액
        'recent_purchase': 0, # 최근 30일간 구매액
        'grade': 0 # 등급
    })

N = int(input())
for _ in range(N):
    date, price = input().split()
    year, month, day = map(int, date.split('/'))
    days = day_of_year(month, day)
    user_info[days - 1]['purchase'] = int(price)

for i in range(365):
    if user_info[i]['purchase'] > 0:
        for j in range(min(30, 365 - i)):
            user_info[i + j]['recent_purchase'] += user_info[i]['purchase']
            user_info[i + j]['grade'] = get_grade(user_info[i + j]['recent_purchase'])

counter = [0] * 5

for i in range(365):
    if user_info[i]['grade'] == BRONZE:
        counter[BRONZE] += 1
    elif user_info[i]['grade'] == SILVER:
        counter[SILVER] += 1
    elif user_info[i]['grade'] == GOLD:
        counter[GOLD] += 1
    elif user_info[i]['grade'] == PLATINUM:
        counter[PLATINUM] += 1
    elif user_info[i]['grade'] == DIAMOND:
        counter[DIAMOND] += 1

print(' '.join(map(str, counter)))
