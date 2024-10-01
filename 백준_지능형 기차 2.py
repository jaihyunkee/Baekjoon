# 0 32
# 3 13
# 28 25
# 17 5
# 21 20
# 11 0
# 12 12
# 4 2
# 0 8
# 21 0

chart = [list(map(int, input().split())) for _ in range(10)]

max_people = 0
cur_train = 0
for base in chart:
    a, b = base[0], base[1]
    cur_train -= a
    cur_train += b
    max_people = max(max_people, cur_train)

print(max_people)
