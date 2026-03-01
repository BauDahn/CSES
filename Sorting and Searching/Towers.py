import sys
from bisect import bisect_right

# sys.stdin = open('input.txt', 'r')

data = sys.stdin.read().split()
it = iter(data)
to_int = int

n = to_int(next(it))

cimas  = [] # Inicializamos la lista de cimas
for i in range(n): # Para cada cajita
    w = to_int(next(it))
    indice = bisect_right(cimas, w)
    
    if indice == len(cimas): # Significa que hay que hacer una torrecita nueva
        cimas.append(w)
        continue # Nos vamos a la pija
    # En caso de que vayamos a ponerlo en la cima de una torre ya existente
    cimas[indice] = w # Nos vamos a la torre correspondiente y lo ponemos ahí :)

print(len(cimas))
