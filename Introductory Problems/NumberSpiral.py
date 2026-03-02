import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().splitlines()

n = int(data[0])
for i in range(1, n + 1):
    x, y = map(int, data[i].split())
    # x es la fila
    # y es la columna

    if x >= y:
        if x % 2 == 0: # Si estamos en una fila par
            print(x**2 - y + 1)
        else: # No estamos en un fila par
            print((x - 1)**2 + y)
    else:
        if y % 2 == 0: # Si estamos en una columna par
            print((y - 1)**2 + x)
        else: # Columna impar   
            print(y**2 - x + 1)
