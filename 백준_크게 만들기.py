N, K = map(int,input().split())

num = str(input())

ans = []
stack = []
ans_length = N - K

leftover = -1
for i, a in enumerate(num):
    if not stack:
        stack.append(a)
    else:
        if int(stack[-1]) < int(a):
            while stack:
                if int(stack[-1]) < int(a):
                    cur_num = int(stack.pop())
                else:
                    break
                # check if the rest numbers meet requirement
                if (len(stack) + (N - i)) == ans_length:
                    leftover = i
                    break
            if leftover != -1:
                break
        stack.append(a)

if leftover != -1:
    temp = num[leftover:]
    for t in temp:
        stack.append(t)

while len(stack) > ans_length:
    stack.pop()

print("".join(stack))



