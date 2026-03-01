import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().split()

it = iter(data)
to_int = int

n = to_int(next(it))
x = to_int(next(it))

coins = []
for i in range(n):
    coins.append(to_int(next(it)))

coins.sort()
max_coin = coins[-1]
MOD = 10**9 + 7

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, min(x, max_coin) + 1):
    suma = 0
    for coin in coins:
        if i < coin:
            break

        suma += dp[i - coin]
    dp[i] = suma % MOD

for i in range(max_coin + 1, x + 1):
    suma = 0
    for coin in coins:
        suma += dp[i - coin]
        
    dp[i] = suma % MOD

print(dp[x])