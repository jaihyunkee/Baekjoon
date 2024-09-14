# 5
# 12 10
# 1B3B3B81F75E
# 16 2
# F53586D76286B2D8
# 20 14
# 88F611AE414A751A767B
# 24 16
# 044D3EBA6A647B2567A91D0E
# 28 11
# 8E0B7DD258D4122317E3ADBFEA99
from collections import deque

T = int(input())

def convert_to_decimal(letters):
    # letter's length is same as iteration
    letters.reverse()
    num = 0
    for i in range(iteration):
        cur_num = letters[i]
        ascii_value = ord(cur_num)
        # number
        if 48 <= ascii_value <= 57:
            num += (ascii_value - 48) * (16 ** i)
        # alphabet
        elif 65 <= ascii_value <= 70:
            num += (ascii_value - 55) * (16 ** i)
    letters.reverse()
    return num


def count_unqiue(target):

    letter = []
    for i, cur_ in enumerate(target):
        if (i+1) % iteration == 0:
            letter.append(cur_)
            converted = convert_to_decimal(letter)
            unique_values[converted] = letter
            letter = []
        else:
            letter.append(cur_)



for test_case in range(1, T + 1):
    N,K = map(int, input().split())
    iteration = N // 4
    nums = input()

    unique_values = {}

    queue = deque()
    for num in nums:
        queue.append(num)

    for _ in range(iteration):
        queue.rotate(1)
        temp = list(queue)
        count_unqiue(temp)

    all_values = list(unique_values.keys())

    all_values.sort(reverse=True)
    target = all_values[K - 1]
    print(f"#{test_case} {target}")
