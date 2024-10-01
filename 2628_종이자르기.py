# 10 8
# 3
# 0 3
# 1 4
# 0 2

col, row = map(int, input().split())
N = int(input())
cuts = [list(map(int, input().split())) for _ in range(N)]

rows = [(-1, row - 1)]
cols = [(-1, col - 1)]

for cut in cuts:
    a, b = cut
    index = b - 1
    if a == 0:
        to_remove = None
        for row_ in rows:
            from_, to_ = row_
            if from_ < index < to_:
                to_remove = row_
                rows.append((from_, index))
                rows.append((index, to_))
                break
        if to_remove:
            rows.remove(to_remove)
    else:
        to_remove = None
        for col_ in cols:
            from_, to_ = col_
            if from_ < index < to_:
                to_remove = col_
                cols.append((from_, index))
                cols.append((index, to_))
                break
        if to_remove:
            cols.remove(to_remove)


rows.sort(key=lambda x: -(x[1] - x[0]))
cols.sort(key=lambda x: -(x[1] - x[0]))

row_a, row_b = rows[0]
col_a, col_b = cols[0]

print((row_b - row_a) * (col_b - col_a))