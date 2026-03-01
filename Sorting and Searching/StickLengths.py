import sys

sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int

n = to_int(next(it))

lista = []
for i in range(n):
    lista.append(to_int(next(it)))

lista.sort()
target = lista[n // 2]
suma = 0
for numero in lista:
    suma += abs(numero - target)

print(suma)