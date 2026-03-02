import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().split()

n = int(data[0])
lista = list(map(int, data[1:]))

# Recorremos el array y vamos sumando diferencias si el siguiente es mayor
movimientos = 0
for i in range(n - 1):
    numero = lista[i] # Agarramos el número actual
    siguiente = lista[i + 1]
    if numero > siguiente: # Si el número es mayor que el que sigue
        movimientos += numero - siguiente
        lista[i + 1] = numero

print(movimientos)