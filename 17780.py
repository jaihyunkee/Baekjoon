from collections import deque

def can_move(cur_pos1, dir1):
    if cur_pos1[0] + dir1[0] - 1 < 0 or cur_pos1[0] + dir1[0] - 1 >= N or cur_pos1[1] + dir1[1] - 1 < 0 \
            or cur_pos1[1] + dir1[1] - 1 >= N:
        return 0
    else:
        return 1

def reverse(direction1):
    if direction1 == 1:
        return 2
    elif direction1 == 2:
        return 1
    elif direction1 == 3:
        return 4
    elif direction1 == 4:
        return 3

def check_(pawns1, board_queue_):
    for k in range(len(pawns1)):
        x, y, _ = pawns1[k]
        if len(board_queue_[x - 1][y - 1]) >= 4:
            return 1
    return 0



check = 0
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board_queue = [[deque() for _ in range(N)] for _ in range(N)]
pawns = []
for _ in range(K):
    pawns.append(tuple(map(int, input().split())))


for i in range(len(pawns)):
    x, y, direction = pawns[i]
    board_queue[x - 1][y - 1].append(i)
round_ = 0

while round_ < 1000:
    round_ += 1
    for i in range(len(pawns)):
        x, y, direction = pawns[i]
        current_queue = board_queue[x - 1][y - 1]
        if len(current_queue) != 0 and i == current_queue[0]:
            # 1: right 2: left
            # 3: up    4: down
            modification = [0, 0]
            if direction == 1:
                modification = [0, 1]
            elif direction == 2:
                modification = [0, -1]
            elif direction == 3:
                modification = [-1, 0]
            elif direction == 4:
                modification = [1, 0]

            new_pos = [x + modification[0], y + modification[1]]

            if can_move([x, y], modification):
                # white: move
                if board[new_pos[0] - 1][new_pos[1] - 1] == 0:
                    if len(board_queue[x - 1][y - 1]) != 0:
                        while board_queue[x - 1][y - 1]:
                            temp = board_queue[x - 1][y - 1].popleft()
                            pawns[temp] = (new_pos[0], new_pos[1], pawns[temp][2])
                            board_queue[new_pos[0] - 1][new_pos[1] - 1].append(temp)

                # red: move and reverse
                elif board[new_pos[0] - 1][new_pos[1] - 1] == 1:
                    if len(board_queue[x - 1][y - 1]) != 0:
                        while board_queue[x - 1][y - 1]:
                            temp = board_queue[x - 1][y - 1].pop()
                            pawns[temp] = (new_pos[0], new_pos[1], pawns[temp][2])
                            board_queue[new_pos[0] - 1][new_pos[1] - 1].append(temp)
                # blue: change direction and move check if opposite is also blue if so dont move
                else:
                    opposite_ = [x + modification[0] * -1, y + modification[1] * -1]
                    pawns[i] = (x, y, reverse(direction))
                    if can_move([x, y], [modification[0] * -1,modification[1] * -1]):
                        # check if opposite is also blue
                        if board[opposite_[0] - 1][opposite_[1] - 1] == 2:
                            continue
                        # white
                        elif board[opposite_[0] - 1][opposite_[1] - 1] == 0:
                            if len(board_queue[x - 1][y - 1]) != 0:
                                while board_queue[x - 1][y - 1]:
                                    temp = board_queue[x - 1][y - 1].popleft()
                                    pawns[temp] = (opposite_[0], opposite_[1], pawns[temp][2])
                                    board_queue[opposite_[0] - 1][opposite_[1] - 1].append(temp)
                        # red
                        else:
                            if len(board_queue[x - 1][y - 1]) != 0:
                                while board_queue[x - 1][y - 1]:
                                    temp = board_queue[x - 1][y - 1].pop()
                                    pawns[temp] = (opposite_[0], opposite_[1], pawns[temp][2])
                                    board_queue[opposite_[0] - 1][opposite_[1] - 1].append(temp)
                    else:
                        continue
            else:
                opposite_ = [x + modification[0] * -1, y + modification[1] * -1]
                pawns[i] = (x, y, reverse(direction))
                if can_move([x, y], [modification[0] * -1, modification[1] * -1]):
                    # check if opposite is also blue
                    if board[opposite_[0] - 1][opposite_[1] - 1] == 2:
                        continue
                    # white
                    elif board[opposite_[0] - 1][opposite_[1] - 1] == 0:
                        if len(board_queue[x - 1][y - 1]) != 0:
                            while board_queue[x - 1][y - 1]:
                                temp = board_queue[x - 1][y - 1].popleft()
                                pawns[temp] = (opposite_[0], opposite_[1], pawns[temp][2])
                                board_queue[opposite_[0] - 1][opposite_[1] - 1].append(temp)
                    # red
                    else:
                        if len(board_queue[x - 1][y - 1]) != 0:
                            while board_queue[x - 1][y - 1]:
                                temp = board_queue[x - 1][y - 1].pop()
                                pawns[temp] = (opposite_[0], opposite_[1], pawns[temp][2])
                                board_queue[opposite_[0] - 1][opposite_[1] - 1].append(temp)
                else:
                    continue

        if check_(pawns, board_queue) == 1:
            break
    if check_(pawns, board_queue) == 1:
        break

if round_ < 1000:
    print(f"{round_}")
else:
    print("-1")

