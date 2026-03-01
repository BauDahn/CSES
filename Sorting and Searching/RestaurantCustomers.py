import sys

sys.stdin = open('input.txt', 'r')
to_int = int

data = sys.stdin.read().split()

it = iter(data)
n = int(next(it))

llegadas = []
salidas = []

for _ in range(n):
    llegadas.append(to_int(next(it)))
    salidas.append(to_int(next(it)))

llegadas.sort()
salidas.sort()

max_clientes = 0
clientes_actuales = 0
i = 0
j = 0

while i < n: # i recorre las llegadas
    if llegadas[i] <= salidas[j]: # Si llega antes o al mismo tiempo que el otro sale
        clientes_actuales += 1
        i += 1
        if clientes_actuales > max_clientes:
            max_clientes = clientes_actuales
    else: # El siguiente evento mas cercano es una salida
        clientes_actuales -= 1
        j += 1
        


print(max_clientes)