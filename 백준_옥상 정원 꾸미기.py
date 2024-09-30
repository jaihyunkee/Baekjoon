# 6
# 10
# 3
# 7
# 4
# 12
# 2
N = int(input())
buildings = []

for _ in range(N):
    buildings.append(int(input()))

ans = [0 for _ in range(N)]
stack = []
i = 0
while i < N:
    if not stack:
        stack.append((i, buildings[i]))
    else:
        if stack[-1][1] <= buildings[i]:
            while stack:
                if stack[-1][1] > buildings[i]:
                    break
                a,b = stack.pop()
                ans[a] = i - a - 1
        stack.append((i, buildings[i]))
    i += 1

while stack:
    a, b = stack.pop()
    ans[a] = i - a - 1

print(sum(ans))