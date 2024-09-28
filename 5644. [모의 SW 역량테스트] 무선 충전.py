from itertools import product


def calculate(A_, B_):
    max_comb = None
    max_ = -1
    for comb in product(A_, B_):
        first, second = comb
        if first == second:
            _, p = BCs[first]
            if p > max_:
                max_ = p
                max_comb = (first, second)
        else:
            _, p1 = BCs[first]
            _, p2 = BCs[second]
            if p1 + p2 > max_:
                max_ = p1 + p2
                max_comb = (first, second)
    return max_comb, max_



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M,N = map(int,input().split())
    A_path = list(map(int,input().split()))
    B_path = list(map(int,input().split()))

    #  0, 1 = 상, 2 = 우, 3 = 하, 4 = 좌

    dxs, dys = [-1,0,1,0], [0,1,0,-1]
    BCs = {}
    for _ in range(N):
        a,b,c,p = map(int, input().split())
        BCs[(b-1,a-1)] = (c, p)
    A = [0, 0]
    B = [9, 9]
    grid = [[0 for _ in range(10)] for _ in range(10)]
    ans = 0

    for i in range(M + 1):
        A_possible_BCs = []
        B_possible_BCs = []
        for key in BCs.keys():
            a,b = key
            c,p = BCs[key]
            # in range
            if abs(a - A[0]) + abs(b - A[1]) <= c:
                A_possible_BCs.append(key)
            if abs(a - B[0]) + abs(b - B[1]) <= c:
                B_possible_BCs.append(key)
        local_max = 0
        if len(A_possible_BCs) != 0 and len(B_possible_BCs) != 0:
            comb, local_max = calculate(A_possible_BCs, B_possible_BCs)
        elif len(A_possible_BCs) == 0 and len(B_possible_BCs) != 0:
            temp_max = 0
            for key in B_possible_BCs:
                _, p1 = BCs[key]
                temp_max = max(temp_max, p1)
            local_max = temp_max
        elif len(A_possible_BCs) != 0 and len(B_possible_BCs) == 0:
            temp_max = 0
            for key in A_possible_BCs:
                _, p1 = BCs[key]
                temp_max = max(temp_max, p1)
            local_max = temp_max
        ans += local_max
        # print(i, local_max)

        if i == M:
            break
        if A_path[i] == 0 and B_path[i] == 0:
            continue
        elif A_path[i] != 0 and B_path[i] == 0:
            dxA, dyA = dxs[A_path[i] - 1], dys[A_path[i]-1]
            A[0], A[1] = A[0] + dxA, A[1] + dyA
        elif A_path[i] == 0 and B_path[i] != 0:
            dxB, dyB = dxs[B_path[i] - 1], dys[B_path[i]- 1]
            B[0], B[1] = B[0] + dxB, B[1] + dyB
        else:
            dxA, dyA = dxs[A_path[i] - 1], dys[A_path[i]-1]
            dxB, dyB = dxs[B_path[i] - 1], dys[B_path[i]- 1]

            # current position
            A[0], A[1] = A[0] + dxA, A[1] + dyA
            B[0], B[1] = B[0] + dxB, B[1] + dyB

    print(f"#{test_case} {ans}")


