import sys

# sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int
MOD = 10**9 + 7

n = to_int(next(it))
x = to_int(next(it))

dp = [0] * (x + 1)
dp[0] = 1

for _ in range(n):
    coin = to_int(next(it))

    for i in range(coin, x + 1):
        dp[i] = (dp[i] + dp[i - coin]) % MOD

print(dp[x])