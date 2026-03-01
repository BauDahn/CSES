import sys

# sys.stdin = open('input.txt', 'r')

to_int = int
data = sys.stdin.read().split()

it = iter(data)
n = to_int(next(it))

lista = []
for _ in range(n):
    lista.append(to_int(next(it)))

suma_maxima = lista[0]
suma_actual = 0

for i in range(n):
    if suma_actual < 0: # Si el numero que sigue sirve para hacer la suma mas grande
        suma_actual = lista[i]
    else: # Si el numero que sigue hace que la suma actual siga siendo mayor que 0
        suma_actual += lista[i]

    if suma_actual > suma_maxima:
        suma_maxima = suma_actual

print(suma_maxima)