T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [100000 for _ in range(len(plan))]
    for i in range(len(plan)):

        if i == 1:
            dp[i] = min(dp[i], dp[i - 1] +(prices[0] * plan[i]), dp[i - 1] + prices[1])
        elif i == 0:
            dp[0] = min((prices[0] * plan[i]), prices[1])
        elif i == 2:
            dp[i] = min(dp[i], dp[i - 1] +(prices[0] * plan[i]), dp[i - 1] + prices[1], prices[2])
        else:
            dp[i] = min(dp[i], dp[i - 1] +(prices[0] * plan[i]), dp[i - 1] + prices[1], dp[i-3] + prices[2])


    ans = min(dp[-1], prices[-1])
    print(f"#{test_case} {ans}")
