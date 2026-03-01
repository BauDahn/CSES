import sys

# sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int

n = to_int(next(it))

lista = []
indices = [0] * (n + 1)
for i in range(n):
    num = to_int(next(it))
    lista.append(num)
    # Creacion de la lista de indices
    indices[num] = i

contador = 1
for i in range(2, n + 1):
    if indices[i] < indices[i - 1]: # Queremos recoger el número
        contador += 1

print(contador)