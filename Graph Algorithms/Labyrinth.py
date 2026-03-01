import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

direcciones = [
    (1, 0, 'D'),
    (-1, 0, 'U'),
    (0, 1, 'R'),
    (0, -1, 'L')
]
inv_dir = {'D' : (-1, 0), 'U': (1, 0), 'R' : (0, -1), 'L' : (0, 1)}

mapa = []
for i in range(n):
    mapa.append(list(input().strip()))

visited = [[None]*m for i in range(n)]

q = deque()
inicio = None
final = None

# Encontrar inicio
for i in range(n):
    for j in range(m):
        if mapa[i][j] == 'A':
            inicio = (i, j)
            visited[i][j] = 'A'
            q.append((i, j))
            break

# Bfs
encuentro = False
while q:
    u, v = q.popleft()

    for nr, nc, d in direcciones:
        dr, dc = nr + u, nc + v

        if 0 <= dr < n and 0 <= dc < m and visited[dr][dc] is None:
            if mapa[dr][dc] != '#':
                q.append((dr, dc))
                visited[dr][dc] = d

                if mapa[dr][dc] == 'B':
                    final = (dr, dc)
                    encuentro = True
                    break
    if encuentro:
        break                

if encuentro:
    ruta = []
    i, j = final
    while (i, j) != inicio:
        d = visited[i][j]
        ruta.append(d)
        # BackTracking con calculo
        dr, dc = inv_dir[d]
        i += dr
        j += dc

    print("YES")
    print(len(ruta))
    print("".join(ruta[::-1]))
else:
    print("NO")


