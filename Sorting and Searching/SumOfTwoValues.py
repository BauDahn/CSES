import sys

# sys.stdin = open('input.txt', 'r')

to_int = int
data = sys.stdin.read().split()
it = iter(data)

n = to_int(next(it))
x = to_int(next(it))

lista = []
for _ in range(n):
    lista.append((to_int(next(it)), _ + 1))

lista = sorted(lista, key=lambda x: x[0])

left = 0
right = n - 1

while left < right: # Hasta que los punteros se crucen
    suma = lista[left][0] + lista[right][0]
    if suma > x:
        right -= 1
    elif suma < x:
        left += 1
    else:
        print(lista[left][1], lista[right][1])
        break

if left == right:
    print("IMPOSSIBLE")
