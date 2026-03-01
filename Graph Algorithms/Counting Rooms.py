import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
casa = []
visited = []
for i in range(n):
    casa.append(list(input()))
    visited.append([False for _ in range(m)])
 
contador = 0
direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
 
for i in range(n):
    for j in range(m):
        if casa[i][j] == '.' and visited[i][j] == False:
            contador += 1
            stack = [(i, j)]
            visited[i][j] = True
 
            while stack:
                r, c = stack.pop()
 
                for dr, dc in direcciones:
                    nr, nc = r + dr, c + dc
 
                    if 0 <= nr < n and 0 <= nc < m and casa[nr][nc] == '.':
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
 
print(contador)
 
