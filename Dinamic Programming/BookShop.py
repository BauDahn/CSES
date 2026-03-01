import sys

# sys.stdin = open('input.txt', 'r')
data = sys.stdin.read().split()

n = int(data[0])
x = int(data[1])

precios = list(map(int, data[2 : n + 2]))
hojas = list(map(int, data[n + 2 : ]))


'''
Primer enfoque (Array 2D)

dp = [[0] * (x + 1) for i in range(n)] # Me creo el grid de dp

for i in range(n): # Para cada libro (el algoritmo pasa a ser lineal)
    for j in range(x + 1): # Para cada capacidad
        precio_actual = precios[i] # El precio del libro actual
        if precio_actual > j: # Si el precio actual es mayor que el precio que podemos meter ahora
            if i > 0: # Si no es el primer libro
                dp[i][j] = dp[i - 1][j] # Metemos el de arriba en este
            continue # Huimos xd
            
        if i > 0: # No estamos en la primera fila
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - precios[i]] + hojas[i])
            continue
        # Estamos en la primera fila
        dp[i][j] = hojas[i]



print(dp[n - 1][x])


'''
'''
Segundo enfoque (Array 1D)
'''

dp = [0] * (x + 1) # Creamos el array dp de 1 sola dimensión
max_alcanzable = 0

for p, h in zip(precios, hojas): # Para cada libro

    for j in range(x, p - 1, -1): # Para cada presupuesto (empezando del mayor posible)
        # El dp en la posicion j debe darme la cantidad de paginas que puedo conseguir como maximo con ese presupuesto
        if dp[j] < dp[j - p] + h:
            dp[j] = dp[j - p] + h

print(dp[x])
