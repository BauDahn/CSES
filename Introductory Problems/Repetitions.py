import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read()

contadorTotal = 1
contador = 1
for i in range(len(data) - 1):
    letraActual = data[i]
    if letraActual == data[i + 1]:
        contador += 1
        contadorTotal = max(contadorTotal, contador)
    else:
        contador = 1

print(contadorTotal)
    