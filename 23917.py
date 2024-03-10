col, row, col_s, row_s = map(int, input().split())


row_count = 0
col_count = 0
#original
while row > 0:
    row -= 1
    row_count += 1
    row -= row_s

while col > 0:
    col -= 1
    col_count += 1
    col -= col_s
# optimization

col_count = (col + col_s) // (1 + col_s)
row_count = (row + row_s) // (1 + row_s)
print(row_count * col_count)