import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for i in range(n)]
equipos = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

for i in range(n):
    if equipos[i] == 0: # No ha sido explorado
        q = deque([i]) # Voy a inicializar una cola desde el nodo i para hacer un bfs (explorar sus vecinos)
        equipos[i] = 1 # Lo pongo al equipo 1 por predeterminado

        while q:
            u = q.popleft()
            for v in adj[u]:
                if equipos[v] == 0: # El equipo adyacente esta inexplorado
                    equipos[v] = 3 - equipos[u] # Lo asigno al equipo contrario
                    q.append(v)
                elif equipos[v] == equipos[u]:
                    print("IMPOSSIBLE")
                    exit()

print(" ".join(map(str, equipos[::])))