from collections import deque

# 입력 받기
grid = [list(input()) for _ in range(8)]

# 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우, 고정
dxs = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dys = [0, 0, -1, 1, -1, 1, -1, 1, 0]

# 초기 시작 위치와 목표 위치
start = (7, 0)
end = (0, 7)

# 벽 위치 저장
walls = []
for i in range(8):
    for j in range(8):
        if grid[i][j] == '#':
            walls.append((i, j))
# 벽을 아래로 이동시키기 위해 reverse 정렬
walls.sort(reverse=True)

# 초기 캐릭터 위치
character = set([start])

# 범위 체크 함수
def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# 벽을 한 칸 아래로 이동시키는 함수
def wall_down():
    global walls
    new_walls = []
    for (x, y) in walls:
        # 벽이 아래로 이동
        if in_range(x + 1, y):
            new_walls.append((x + 1, y))
    walls = new_walls

# BFS 탐색 함수
def bfs():
    queue = deque([character])
    while queue:
        current_set = queue.popleft()

        # 벽이 더 이상 없으면 도달 가능
        if not walls:
            return 1

        next_set = set()
        # 현재 캐릭터 위치들에 대해 이동 시도
        for (x, y) in current_set:
            for dx, dy in zip(dxs, dys):
                cx, cy = x + dx, y + dy
                # 범위 내이고, 벽이 없으며, 이동하지 않은 곳이라면
                if in_range(cx, cy) and (cx, cy) not in walls:
                    # 목표 위치에 도달한 경우
                    if (cx, cy) == end:
                        return 1
                    next_set.add((cx, cy))

        # 벽을 한 칸 아래로 이동
        wall_down()

        # 벽이 캐릭터를 덮친 경우, 해당 캐릭터 제거
        next_set = {pos for pos in next_set if pos not in walls}

        # 더 이상 이동할 수 있는 위치가 없는 경우 실패
        if not next_set:
            return 0

        # 다음 탐색을 위해 큐에 추가
        queue.append(next_set)

    # BFS가 종료될 때까지 도달하지 못하면 실패
    return 0

# 결과 출력
print(bfs())
