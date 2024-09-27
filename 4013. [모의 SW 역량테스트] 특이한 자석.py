from collections import deque
from copy import deepcopy

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

mapping = {0: [1], 1:[0,2], 2:[1,3], 3: [2]}
for test_case in range(1, T + 1):
    K = int(input())
    wheels = [list(map(int, input().split())) for _ in range(4)]
    command = [tuple(map(int, input().split())) for _ in range(K)]

    first_w = deque(wheels[0])
    second_w = deque(wheels[1])
    third_w = deque(wheels[2])
    fourth_w = deque(wheels[3])

    wheels = []

    wheels.append(first_w)
    wheels.append(second_w)
    wheels.append(third_w)
    wheels.append(fourth_w)

    commands = deque()

    update = deepcopy(wheels)

    for ith, direction in command:
        commands.append((ith - 1, direction))
        visited = set()
        after = -1

        # before == 1 = N, 2 = S
        while commands:
            i, command = commands.popleft()
            cur_w = wheels[i]
            visited.add(i)


            update[i].rotate(command)

            to_visit = mapping[i]
            for v in to_visit:
                if v > i:
                    if list(wheels[v])[-2] != list(wheels[i])[2] and v not in visited:
                        commands.append((v, command * -1))
                elif v < i:
                    if list(wheels[v])[2] != list(wheels[i])[-2] and v not in visited:
                        commands.append((v, command * -1))


        wheels = deepcopy(update)

    ans = 0
    for i in range(4):
        point = wheels[i].popleft()
        ans += point * (2 ** i)

    print(f"#{test_case} {ans}")


