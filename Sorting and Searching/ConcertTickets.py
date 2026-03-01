import sys
from bisect import bisect_right

def find(i):
    if i < 0:
        return -1
    if padre[i] == i: # El ticket no ha sido vendido
        return i
    # En el caso de que si que haya sido vendido
    padre[i] = find(padre[i])
    return padre[i]

sys.setrecursionlimit(200005)
input = sys.stdin.readline

n, m = map(int, input().split())

padre = list(range(n + 1)) # Creo la lista de padres

precios_tickets = list(map(int, input().split()))

maximos = list(map(int, input().split()))

'''
Metodología:
lista para poder conseguir el indice = [precios_tickets]
diccionario para tener las frecuencias
'''
precios_tickets.sort() # La sorteamos para poder usarla para encontrar indices

resultado = []
for maximo in maximos:
    indice = bisect_right(precios_tickets, maximo) - 1
    indice_real = find(indice)

    if indice_real != -1: # Hay un ticket para esta persona disponible
        resultado.append(str(precios_tickets[indice_real]))
        padre[indice_real] = find(indice_real - 1)
    else:
        resultado.append("-1")

sys.stdout.write('\n'.join(resultado))
            

