from copy import deepcopy

def dfs(ll, resource):
    global unique_combinations
    if len(resource) == 0:
        unique_combinations.append(ll)
    re_set = set(resource)
    for ele in re_set:
        cur_po = deepcopy(resource)
        cur_po.remove(ele)

        cur_ans = deepcopy(ll)
        cur_ans.append(ele)
        dfs(cur_ans, cur_po)



def calculate(possibles):
    all_possible = []
    possibles.sort()
    for cur in possibles:
        count = 1
        cur_ans = nums[0]
        for idx, express in enumerate(cur):
            if express == "+":
                cur_ans = cur_ans + nums[count]
            if express == "-":
                cur_ans = cur_ans - nums[count]
            if express == "*":
                cur_ans = cur_ans * nums[count]
            if express == "/":
                if nums[count] != 0:
                    cur_ans = int(cur_ans / nums[count])
                else:
                    cur_ans = 0
                    break
            count += 1
        all_possible.append(cur_ans)

    min_, max_ = min(all_possible), max(all_possible)
    return (max_ - min_)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # +, -, *, /
    exp = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    expression = ["+", "-", "*", "/"]
    total = []
    for i in range(4):
        for j in range(exp[i]):
            total.append(expression[i])
    unique_combinations = []
    dfs([], total)

    f_ans = calculate(unique_combinations)
    print(f"#{test_case} {f_ans}")