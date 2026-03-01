import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

aplicantes = list(map(int, input().split()))
apartamentos = list(map(int, input().split()))

aplicantes.sort(reverse=False)
apartamentos.sort(reverse=False)

contador = 0
i = 0
j = 0
while j < m and i < n:
    if aplicantes[i] > apartamentos[j] + k: # Si el departamento es demasiado chico
        j += 1 # Paso al proximo apartamento
    elif aplicantes[i] < apartamentos[j] - k: # Si el departamento es demasiado grande
        i += 1 # Paso al proximo aplicante
    else:
        i += 1
        j += 1
        contador += 1

print(contador)