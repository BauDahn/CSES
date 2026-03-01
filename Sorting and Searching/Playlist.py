import sys
 
# sys.stdin = open('input.txt', 'r')
 
data = sys.stdin.read().split()
to_int = int
it = iter(data)
 
n = to_int(next(it))
 
# Creamos la lista con las canciones
lista = []
for i in range(n):
    lista.append(to_int(next(it)))
 
# Inicializamos punteros y diccionario
i = 0
j = 0
dic = {}
maximo = 0
 
# Hasta terminar de recorrer la lista
while j < n:
    id = lista[j]
 
    if id in dic: # Si la canción ya está en el diccionario
        i = max(i, dic[id] + 1)
    
    dic[id] = j
    maximo = max(maximo, j - i + 1)
 
    j += 1
 
print(maximo)
