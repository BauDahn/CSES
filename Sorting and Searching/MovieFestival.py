import sys

# sys.stdin = open('input.txt', 'r')

to_int = int
data = sys.stdin.read().split()

it = iter(data)

n = to_int(next(it))

pelis = []
for _ in range(n):
    pelis.append((to_int(next(it)), to_int(next(it))))

pelis = sorted(pelis, key=lambda x: x[1])
hora_libre_actual = 0
contador_pelis = 0

for inicio, fin in pelis:
    if inicio >= hora_libre_actual:
        contador_pelis += 1
        hora_libre_actual = fin

print(contador_pelis)

