from copy import deepcopy
from itertools import product, combinations


def calculate(ll):
    ans = 0
    for aa in range(1, M+1):
        for comb in combinations(ll, aa):
            if sum(comb) > C:
                continue
            else:
                cur_max = 0
                for element in comb:
                    cur_max += element ** 2
                ans = max(ans, cur_max)

    return ans

T = int(input())
for test_case in range(1, T + 1):
    N,M,C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_each_rows = []
    for i in range(N):
        curr = grid[i]
        max_ = -1
        for j in range(M, N + 1):
            curr_value = calculate(curr[j-M:j])
            max_ = max(curr_value, max_)
        max_each_rows.append(max_)

    max_each_rows.sort()
    each_row_max = max_each_rows[-1] + max_each_rows[-2]
    for i in range(N):
        curr = grid[i]
        first = [0, M]
        second = [M, M+M]
        count = 0
        while M+M+count < N:
            first = [first[0] + count, first[1] + count]
            second  = [second[0] + count, second[1] + count]

            test = calculate(curr[first[0]:first[1]]) + calculate(curr[second[0]:second[1]])
            each_row_max = max(each_row_max, test)
            count += 1

    print(f"#{test_case} {each_row_max}")

