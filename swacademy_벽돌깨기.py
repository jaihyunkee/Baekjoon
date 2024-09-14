# 가장 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
#
# 그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
#
# 각 테스트 케이스의 첫 번째 줄에는 N, W, H 가 순서대로 공백을 사이에 두고 주어지고,
#
# 다음 H 줄에 걸쳐 벽돌들의 정보가 1 줄에 W 개씩 주어진다.
from collections import deque
from copy import deepcopy
from itertools import product

dxs = [-1,1,0,0]
dys = [0,0,1,-1]

def count_(grid_copy):
    count = 0
    for i in range(H):
        for j in range(W):
            if grid_copy[i][j] != 0:
                count += 1
    return count

def in_range(x,y):
    return 0 <= x < H and 0 <= y < W

def bfs(x,y, target, grid_copy):
    queue = deque()
    queue.append((x,y))
    visited = set()
    visited.add((x,y))

    while queue:
        xx, yy = queue.popleft()
        visited.add((xx,yy))
        target = grid_copy[xx][yy]
        grid_copy[xx][yy] = 0
        for i in range(target):
            for dx, dy in zip(dxs, dys):
                cx, cy = xx + dx * i, yy + dy * i
                if in_range(cx, cy) and (cx, cy) not in visited and (cx, cy) not in queue and grid_copy[cx][cy] != 0:
                    queue.append((cx,cy))



def shoot(index, grid_copy):
    for i in range(H):
        if grid_copy[i][index] != 0:
            target = grid_copy[i][index]
            bfs(i,index, target, grid_copy)
            break
    return grid_copy

def gravity(grid_copy):
    for j in range(W):
        temp = []
        for i in range(H-1, -1, -1):
            if grid_copy[i][j] != 0:
                temp.append(grid_copy[i][j])
        count = 0
        for i in range(H-1, -1, -1):
            if count < len(temp):
                grid_copy[i][j] = temp[count]
                count += 1
            else:
                grid_copy[i][j] = 0

    return grid_copy


def simulate(comb):
    grid_copy = deepcopy(grid)
    for index in comb:
        grid_copy = shoot(index, grid_copy)
        grid_copy = gravity(grid_copy)

    return count_(grid_copy)





T = int(input())

for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    min_ = 10000000
    for combination in product([i for i in range(W)], repeat=N):
        if min_ == 0:
            break
        min_ = min(min_, simulate(combination))

    print(f"#{test_case} {min_}")