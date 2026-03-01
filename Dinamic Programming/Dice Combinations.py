import sys
 
input = sys.stdin.readline
 
n = int(input())
MOD = 10**9 + 7
 
'''
Creo una tabla dp. Es una tabla donde escribo de cuantas formas puedo sumar el numero i
dp[i] significa de cuantas formas puedo formar el numero i, por lo que es recursiva en cierta medida
El numero máximo de formas me lo va a decir dp[n]
'''
 
dp = [0] * (n + 1) # Creo la tabla inicializada en 0
dp[0] = 1 # Caso base. De cuantas formas podemos formar el 0 en el caso 0. 1, sin tirar dados
 
# Rellenaremos la tabla
for i in range(1, n + 1): # Resolvemos para el numero i
    for dado in range(1, 7): # Calculamos los 6 saltos posibles que podemos dar
        '''
        Las formas de llegar al escalon i son la suma de
        todas las formas de haber llegado a los escalones desde los que puedo saltar a i
        '''
        if i - dado >= 0: # Evitamos mirar indices negativos, no podemos venir del -2
            # dp[4] = dp[3] + dp[2] + dp[1] + dp[4]
            dp[i] = (dp[i] + dp[i - dado]) % MOD
 
 
print(dp[n])
