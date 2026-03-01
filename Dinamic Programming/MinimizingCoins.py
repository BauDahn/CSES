import sys

input= sys.stdin.readline

n, x = map(int, input().split())

coins = list(map(int, input().split()))

dp = [10**8] * (x + 1)
dp[0] = 0


for coin in coins:
    for i in range(coin, x + 1):
        if dp[i - coin] + 1 < dp[i]:
            dp[i] = dp[i - coin] + 1

if dp[x] == 10**8:
    print(-1)
else:
    print(dp[x])