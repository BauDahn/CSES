import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().splitlines()
it = iter(data)
to_int = int

n = to_int(next(it))
MOD = 10**9 + 7

grid = []

for i in range(n):
    grid.append((next(it)))

dp = [[0] * n for i in range(n)]
if grid[0][0] != '*': # Cuidado con que la primer casilla sea una trampa
    dp[0][0] = 1 # hay una forma de llegar a la primer casilla (no moverse)

for x in range(n):
    for y in range(n):

        if grid[x][y] == '*': # Si estamos en una trampa
            dp[x][y] = 0 # No hay forma de llegar ahí
            continue
        # En el caso de no estar en una trampa
        if x > 0:
            dp[x][y] += dp[x - 1][y]
        
        if y > 0:
            dp[x][y] += dp[x][y - 1]
        
        dp[x][y] %= MOD

print(dp[n - 1][n - 1])


