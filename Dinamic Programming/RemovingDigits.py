import sys

n = int(sys.stdin.read())

contador = 0
while n > 0:
    n = str(n)
    digito_mayor = int(max(n)) # Me quedo con el digito mayor

    n = int(n)

    n -= digito_mayor
    contador += 1

print(contador)
