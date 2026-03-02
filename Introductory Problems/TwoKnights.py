n = int(input())

'''
Explicación del código:
Del tablero entero, solo tengo un número x de formas de que los caballos se ataquen.
El problema se reduce a ver el número de posiciones posibles y restarle todas las que los caballos se ataquen.
El número de posiciones posibles se calcula con combinatoria.
El tablero es de k x k, eso da k**2 posiciones.
Con 2 caballos, el número de posiciones posibles se calcula como: (k^2 x (k^2 - 1)) / 2
Luego las formas de los caballos de atacarse se dividen en dos tipos:
-> Se atacan en horizontal -> Necesitan 2 filas x 3 columnas (2x3)
-> Se atacan en vertical -> Necesitan 3 filas x 2 columnas (3x2)
En cada una de las formas siempre se atacan exactamente de dos formas distintas
Ahora bien, podemos ver la cantidad total de formas como la cantidad de bloques horizontales que entran en el array por la cantidad de bloques verticales
-> Esto se calcula como: (k-1)(k-2)
-> La formula final es: (k^2 x (k^2-1))/2 - 2 * 2 * (k-1) * (k - 2)
'''
for i in range(1, n + 1):
    if i == 1:
        print(0)
        continue
    print((i**4 - i**2)//2 - 4*(i**2 - 3*i + 2))