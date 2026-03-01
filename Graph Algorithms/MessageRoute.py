import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

lista = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    lista[a - 1].append(b - 1)
    lista[b - 1].append(a - 1)

print(lista)

visited = [-2] * n

print(visited)

q = deque()
q.append(0)
visited[0] = -1

# Bfs
encuentro = False
while q:
    nodo = q.popleft()
    
    if nodo == n - 1:
        encuentro = True
        break

    for vecino in lista[nodo]:
        if visited[vecino] == -2: # Si no ha sido visitado
            visited[vecino] = nodo # Pongo en la lista dentro de visited asociada al vecino del nodo el nodo del que viene
            q.append(vecino)

if encuentro:
    ruta = []
    nodo = n - 1

    while nodo != -1:
        ruta.append(nodo + 1)
        nodo = visited[nodo]
    
    print(len(ruta))
    print(' '.join(map(str, ruta[::-1])))

else:
    print("IMPOSSIBLE")