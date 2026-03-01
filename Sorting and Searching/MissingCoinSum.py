import sys

# sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int

n = to_int(next(it))
lista = []
for i in range(n):
    lista.append(to_int(next(it)))

lista.sort()
r = lista[0]
if r != 1:
    print(1)
    exit()
for i in range(1, n):
    if r + 1 >= lista[i]:
        r += lista[i]
    else: # r < lista[i] + 1
        break

print(r + 1)