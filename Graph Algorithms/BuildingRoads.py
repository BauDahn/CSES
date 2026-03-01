from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n es el numero de ciudades
# m es el numero de carreteras construidas

dic_rutas = defaultdict(list)

for i in range(m):
    a, b = map(int, input().split())
    dic_rutas[a].append(b)
    dic_rutas[b].append(a)
    # De este forma creo un grafo no dirigido con conexion entre a y b

# Hacer un bfs para encontrar los subarboles dentro del grafo
'''
Crearé una lista para las ciudades visitadas y la iniciaré a False
Luego por cada ciudad visitada la convertiré a True
'''
visited = [False] * (n + 1) # n + 1 porque empiezo a contar desde el 1 y no desde el 0
sol = []

for i in range(1, n + 1): # Para cada ciudad
    if not visited[i]: # Si aun no ha sido visitada
        q = deque([i])
        sol.append(i) # La idea es que cuente las ciudades que identifican los subarboles del grafo
        while q: # Mientras la cola no este vacía
            u = q.popleft() # Agarro el primer elemento (ciudad)
            for v in dic_rutas[u]: # Para cada ciudad adyacente
                if not visited[v]: # Si no fue visitada aun
                    visited[v] = True # Volvemos su posicion en visited a True
                    q.append(v) # Añadimos a la cola la ciudad para mirar luego a que ciudades nos lleva
                
print(len(sol) - 1) # Imprimimos el numero de subarboles del grafo

for a, b in zip(sol[:-1], sol[1:]):
    print(a, b)